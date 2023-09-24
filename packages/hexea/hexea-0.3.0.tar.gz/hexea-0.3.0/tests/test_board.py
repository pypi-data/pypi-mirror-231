from hexea import Yboard, Board, Hexboard, Marker
from copy import copy


YBOARD_SIZE_3 = """
.
   .
.     .
   .
.
"""

YBOARD_SIZE_3_MOVE_1_0 = """
.
   X
.     .
   .
.
"""

YBOARD_SIZE_3_MOVE_1_0_0_2 = """
.
   X
.     .
   .
O
"""

YBOARD_SIZE_3_X_WON = """
O
   X
X     X
   .
O
"""

YBOARD_SIZE_3_O_WON = """
X
   O
O     X
   X
O
"""


def test_yboard_size_3():
    b = Yboard(3)
    assert str(b) == str(YBOARD_SIZE_3)


def test_yboard_size_3_two_moves():
    b = Yboard(3)
    assert b.get_next_player() == Marker.red
    b.move(1, 0)
    assert str(b) == str(YBOARD_SIZE_3_MOVE_1_0)
    assert b.get_next_player() == Marker.blue
    b.move(0, 2)
    assert str(b) == str(YBOARD_SIZE_3_MOVE_1_0_0_2)
    assert b.get_next_player() == Marker.red


def test_x_wins_a_y_game():
    b = Yboard(3).move(1, 0).move(0, 0).move(2, 0).move(0, 2).move(0, 1)
    assert str(b) == str(YBOARD_SIZE_3_X_WON)
    assert b.get_winner() == Marker.red


def test_o_wins_a_y_game():
    b = Yboard(3).move(0, 0).move(0, 1).move(1, 1).move(1, 0).move(2, 0).move(0, 2)
    assert str(b) == str(YBOARD_SIZE_3_O_WON)
    assert b.get_winner() == Marker.blue

def random_playout_tester(b: Board):
    b.random_playout()
    assert b.get_winner() != Marker.none
    assert len(b.get_free_hexes()) == 0

    # Some non-quick random playouts will still fill the board.
    # We run through 1000 random playouts to make it
    # a virtual certainty that one will have empty hexes.
    incomplete_board_found = False
    for _ in range(1000):
        b = Yboard(11)
        b.random_playout(quick=False)
        if len(b.get_free_hexes()) > 0:
            incomplete_board_found = True
            break
    assert incomplete_board_found == True

def test_y_random_playout():
    random_playout_tester(Yboard(11))

def test_hex_random_playout():
    random_playout_tester(Hexboard(11))

def random_playouts_won_tester(b: Board):
    num_playouts = 100
    for quick in (True, False):
        result = b.random_playouts_won(num_playouts, quick=quick)
        assert result[Marker.red] + result[Marker.blue] == num_playouts
        assert len(result) == 2

def test_y_random_playouts_won():
    random_playouts_won_tester(Yboard(11))

def test_hex_random_playouts_won():
    random_playouts_won_tester(Hexboard(11))

def get_list_of_dicts_tester(b: Board):
    num_playouts = 100
    for quick in (True, False):
        result = b.get_list_of_dicts(num_playouts, quick=quick)
        assert len(result) == num_playouts
        assert len([0 for d in result if d['winner'] == Marker.none]) == 0

def test_y_get_list_of_dicts():
    get_list_of_dicts_tester(Yboard(7))

def test_hex_get_list_of_dicts():
    get_list_of_dicts_tester(Hexboard(7))

def test_protocol():
    b = Yboard(5)
    assert isinstance(b, Board)
    h = Hexboard(5)
    assert isinstance(h, Board)


def test_y_get_free_hexes():
    b = Yboard(3)
    expected_free_hexes = set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 0)])
    free_hexes = set(b.get_free_hexes())
    assert expected_free_hexes == free_hexes
    b.move(0, 2)
    expected_free_hexes = set([(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)])
    free_hexes = set(b.get_free_hexes())
    assert expected_free_hexes == free_hexes


HEXBOARD_SIZE_3 = """
 xxxxxxxxxxx
o .   .   . o
 o           o
  o .   .   . o
   o           o
    o .   .   . o
     xxxxxxxxxxx
"""

HEXBOARD_SIZE_3_MOVE_1_0 = """
 xxxxxxxxxxx
o .   X   . o
 o           o
  o .   .   . o
   o           o
    o .   .   . o
     xxxxxxxxxxx
"""

HEXBOARD_SIZE_3_MOVE_1_0_0_2 = """
 xxxxxxxxxxx
o .   X   . o
 o           o
  o .   .   . o
   o           o
    o O   .   . o
     xxxxxxxxxxx
"""

HEXBOARD_SIZE_3_X_WON = """
 xxxxxxxxxxx
o .   X   O o
 o           o
  o .   X   . o
   o           o
    o O   X   . o
     xxxxxxxxxxx
"""

HEXBOARD_SIZE_3_O_WON = """
 xxxxxxxxxxx
o .   X   . o
 o           o
  o O   O   O o
   o           o
    o X   X   . o
     xxxxxxxxxxx
"""


def test_hexboard_size_3():
    b = Hexboard(3)
    assert str(b) == str(HEXBOARD_SIZE_3)


def test_hexboard_size_3_two_moves():
    b = Hexboard(3)
    assert b.get_next_player() == Marker.red
    b.move(1, 0)
    assert str(b) == str(HEXBOARD_SIZE_3_MOVE_1_0)
    assert b.get_next_player() == Marker.blue
    b.move(0, 2)
    assert str(b) == str(HEXBOARD_SIZE_3_MOVE_1_0_0_2)
    assert b.get_next_player() == Marker.red


def test_x_wins_a_hex_game():
    b = Hexboard(3).move(1, 0).move(1, 1).move(1, 2).move(0, 1).move(0, 2).move(2, 1)
    assert str(b) == str(HEXBOARD_SIZE_3_O_WON)
    assert b.get_winner() == Marker.blue


def test_o_wins_a_hex_game():
    b = Hexboard(3).move(1, 1).move(0, 2).move(1, 0).move(2, 0).move(1, 2)
    assert str(b) == str(HEXBOARD_SIZE_3_X_WON)
    assert b.get_winner() == Marker.red

def test_y_board_equality():
    a = Yboard(5)
    b = Yboard(5)
    assert a == b
    a.move(2, 1)
    assert a != b
    b.move(2, 1)
    assert a == b


def test_hex_board_equality():
    a = Hexboard(5)
    b = Hexboard(5)
    assert a == b
    a.move(2, 1)
    assert a != b
    b.move(2, 1)
    assert a == b


def test_y_board_copy():
    a = Yboard(5)
    b = copy(a)
    assert a == b
    b.move(2, 1)
    assert a != b


def test_hex_board_copy():
    a = Hexboard(5)
    b = copy(a)
    assert a == b
    b.move(2, 1)
    assert a != b


def test_hex_get_free_hexes():
    b = Hexboard(3)
    expected_free_hexes = set(
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    )
    free_hexes = set(b.get_free_hexes())
    assert expected_free_hexes == free_hexes
    b.move(1, 1)
    expected_free_hexes = set(
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    )
    free_hexes = set(b.get_free_hexes())
    assert expected_free_hexes == free_hexes

def test_y_get_dict():
    b = Yboard(2)
    d = b.get_dict()
    assert len(d) == 3
    expected_keys = {'cell0_0', 'cell0_1', 'cell1_0'}
    assert set(d.keys()) == expected_keys
    for key in expected_keys:
        assert d[key] == Marker.none
    b.move(0, 1)
    d = b.get_dict()
    assert d['cell0_1'] == Marker.red

def test_hex_get_dict():
    b = Hexboard(2)
    d = b.get_dict()
    assert len(d) == 4
    expected_keys = {'cell0_0', 'cell0_1', 'cell1_0', 'cell1_1'}
    assert set(d.keys()) == expected_keys
    for key in expected_keys:
        assert d[key] == Marker.none
    b.move(0, 1)
    d = b.get_dict()
    assert d['cell0_1'] == Marker.red

