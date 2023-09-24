from typing import Dict, List, Self, Protocol, Tuple, runtime_checkable
from hexea._board import (
    Yboard,
    Marker,
)
from copy import copy

def _marker_to_string(marker: Marker):
    if marker == Marker.red:
        return 'X'
    elif marker == Marker.blue:
        return 'O'
    else:
        return '.'




setattr(Marker, '__str__', _marker_to_string)

@runtime_checkable
class Board(Protocol):
    """
    Protocol defining a game board.  ``Yboard`` and ``Hexboard`` both implement this protocol.
    """

    def __str__(self) -> str:
        ...

    def __copy__(self) -> Self:
        ...

    def get_next_player(self) -> Marker:
        """
        :returns: the player who is allowed to move next

        Returns a :py:class:`Marker` indicating which player is up next:  ``Marker.red`` for an empty
        board, and then alternating between ``Marker.blue`` and ``Marker.red`` as moves are
        played.  Note that this does not change even after a player has won; it is possible to
        keep placing moves as long as there are empty hexes, and even when the board is filled
        up, ``get_next_player()`` will return either ``Marker.red`` or ``Marker.blue``.
        """
        ...

    def move(self, col : int, row : int) -> Self:
        """
        :param col: column of the hex to move to
        :param row: row of the hex to move to
        :returns: ``self`` (for method chaining)

        Places a :py:class:`Marker` representing the next player at the specified column and row.  Throws
        ``IndexError`` if the specified column and row do not exist, and ``ValueError`` if the
        specified location is already occupied.
        """
        ...

    def get_free_hexes(self) -> List[Tuple[int,int]]:
        """
        :returns: A list of tuples indicating the column and row of all free hexes

        Returns a list of 2-tuples, each of which contains the column and row of a hex that is 
        not currently occupied.
        """
        ...

    def random_playout(self, quick: bool=True) -> Self:
        """
        :param quick: boolean indicating whether quick playouts are desired
        :returns: ``self``, after the playout has been run

        Performs a single random playout.  Starting with the current board state, markers for 
        each player are alternately placed on a random hex until no empty hexes are left.

        If ``quick`` is set to ``True`` (the default), a quick playout is generated.  This does
        not check for wins between turns, which means that the resulting board will be
        completely full.  If ``quick`` is set to ``False``, the function will return a result
        as soon as a winning position is reached.
        """
        ...

    def get_dict(self) -> Dict[str, Marker]:
        """
        :returns: a dictionary indicating which marker occupies each hex

        Returns a dictionary whose keys are all strings representing a cell on the board (e.g.,
        ``cell0_0``) and whose values are :py:class:`Marker` objects indicating the occupant of the cell.  
        """
        ...

    def random_playouts_won(self, num_playouts : int, quick: bool=True) -> Dict[Marker, int]:
        """
        :param num_playouts:  number of playouts to run
        :param quick:  boolean indicating whether quick playouts are desired
        :returns: a dictionary indicating how many wins each player had

        Starting with the current board position, runs ``num_playouts`` random playouts.  Returns
        a dictionary whose keys are ``Marker.red`` and ``Marker.blue``, and whose values are the 
        number of wins each player has.
        """
        ...

    def get_winner(self) -> Marker:
        """
        :returns:  the winner of the current board

        Returns a :py:class:`Marker` representing the current winning player, or ``Marker.none`` if the
        board is not yet in a winning state.
        """
        ...

    def get_list_of_dicts(self, num_playouts: int, quick: bool=True) -> List[Dict[str, Marker]]:
        """
        :param num_playouts:  number of playouts to run
        :param quick:  boolean indicating whether quick playouts are desired
        :returns: a list of dictionaries indicating how many wins each player had, and who won

        This is essentially the equivalent of running ``num_playouts`` random playouts and calling
        :py:meth:`Board.get_dict` after each one, then returning the results in a list.  The main difference
        is that each dictionary in the list also contains a ``winner`` item indicating who won.
        This can be useful for creating Pandas dataframes from Hex and Y boards via the
        ``.from_records()`` method, for example to train ML models for evaluating positions.
        """
        ...

class Hexboard:
    """
    :param size: desired board size
    
    Implementation of the :py:class:`Board` protocol representing a Hex board.  The constructor
    will create a ``size`` x ``size`` board.
    """
    def __init__(self, size):
        self.size = size
        self.yboard = Yboard(size * 2)
        for col in range(size):
            height = size - col
            for row in range(height):
                (
                    self.yboard
                    .move(col, row)
                    .move(col, (2 * size - col) - row - 1)
                )

    def _hex_to_y(self, col : int, row : int) -> Tuple[int, int]:
        return (
            col + row + 1,
            self.size - col - 1
        )

    def _y_to_hex(self, col : int, row : int) -> Tuple[int, int]:
        return (
            self.size - row - 1,
            (col - self.size) + row
        )

    def _y_dict_to_hex_dict(self, d: Dict[str, Marker]) -> Dict[str, Marker]:
        result_dict = {}
        for cell, value in d.items():
            if cell == 'winner':
                result_dict[cell] = value
            else:
                y_board_coordinates = [int(x) for x in cell.split('cell')[1].split('_')]
                col, row = self._y_to_hex(*y_board_coordinates)
                if col >= 0 and row >= 0:
                    result_dict[f"cell{col}_{row}"] = value
        return result_dict

    def __getitem__(self, tup: Tuple[int,int]):
        x, y = tup
        return self.yboard[self._hex_to_y(x, y)]

    def __str__(self) -> str:
        board_width = (self.size * 4) - 1
        footer = ("x" * board_width)
        header = " " + footer + "\n"
        separator = "\no" + (" " * board_width) + "o\n"
        # first create rectangular result
        result = header + separator.join(
            [
                "o "
                + "   ".join([str(self[col, row]) for col in range(self.size)])
                + " o"
                for row in range(self.size)
            ]
        ) + "\n" + footer
        # now skew the result
        result = "\n" + "\n".join([
            (" " * (i-1)) + row
            for i, row in enumerate(result.split("\n"))
        ]) + "\n"
        return result


    def __copy__(self) -> Self:
        b = Hexboard(self.size)
        b.yboard = copy(self.yboard)
        return b

    def get_next_player(self) -> Marker:
        return self.yboard.get_next_player()

    def move(self, col: int, row: int) -> Self:
        ycol, yrow = self._hex_to_y(col, row)
        self.yboard.move(ycol, yrow)
        return self

    def get_free_hexes(self):
        free_y_hexes = self.yboard.get_free_hexes()
        return [self._y_to_hex(*x) for x in free_y_hexes]

    def get_winner(self) -> Marker:
        return self.yboard.get_winner()

    def random_playout(self, quick: bool=True) -> Self:
        self.yboard.random_playout(quick)
        return self

    def random_playouts_won(self, num_playouts : int, quick: bool=True) -> Dict[Marker, int]:
        return self.yboard.random_playouts_won(num_playouts, quick=quick)

    def get_dict(self) -> Dict[str, Marker]:
        return self._y_dict_to_hex_dict(self.yboard.get_dict())

    def __eq__(self, other) -> bool:
        return self.yboard == other.yboard

    def get_list_of_dicts(self, num_playouts: int, quick: bool=True) -> List[Dict[str, Marker]]:
        y_list = self.yboard.get_list_of_dicts(num_playouts, quick=quick)
        return list(map(self._y_dict_to_hex_dict, y_list))


