#include <string>
#include <sstream>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <vector>
#include <utility>
#include <random>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/operators.h>

namespace py = pybind11;




enum class Marker {
  red = 1,
  blue = -1, 
  none = 0
};

class Yboard {
  const int size_;
  std::vector<int> column_sizes_;
  Marker current_player_;
  std::vector<Marker> board_;
  public:
    Yboard(const int size);
    Yboard& move(int col, int row);
    Marker get_winner();
    std::string __str__();
    std::vector<std::pair<int,int> > get_free_hexes();
    Yboard& random_playout(bool quick);
    Marker& get_next_player();
    Marker const& operator () (int col, int row) const;
    Marker& operator () (int col, int row);
    std::map<std::string, Marker> get_dict();
    std::map<Marker, int> random_playouts_won(const int num_playouts, bool quick);
    std::vector<std::map<std::string, Marker>> get_list_of_dicts(const int num_playouts, bool quick);
    bool friend operator==(const Yboard& lhs, const Yboard& rhs);
};

Yboard::Yboard(const int size) : size_(size) {
  for (auto x=size_; x > 0; x--) {
    column_sizes_.push_back(x);
    for (auto y=0; y < x; y++) board_.push_back(Marker::none);
  }
  current_player_ = Marker::red;
}

std::string Yboard::__str__() {
  std::string result;
  result += '\n';
  int rows = (size_ * 2) - 1;
  for (int i=0; i<rows; i++) {
    int x = 0;
    if (i % 2 == 1) {
      x++;
      result += "   ";
    }
    int y = i / 2;
    int yy = y;
    int xx = x;
    int min_yy = 0;
    if (i > rows / 2) min_yy = (i - (rows / 2));
    while ((yy >= 0) && (yy >= min_yy)) {
      char repr;
      auto cell_value = (*this)(xx, yy);
      if (cell_value == Marker::red) {
        repr = 'X';
      } else if (cell_value == Marker::blue) {
        repr = 'O';
      } else repr = '.';
      result += repr;
      if ((yy > 0) && (yy > min_yy)) result += "     ";
      xx += 2;
      yy--;
    }
    result += '\n';
  }
  return result;
}

Marker const& Yboard::operator () (int col, int row) const {
  auto index = 0;
  for(auto i=0; i < col; i++) { index += column_sizes_[i]; }
  index += row;
  return board_[index];
}

Marker& Yboard::operator () (int col, int row) {
  auto index = 0;
  for(auto i=0; i < col; i++) { index += column_sizes_[i]; }
  index += row;
  return board_[index];
}

Yboard& Yboard::move(int col, int row) {
  if (col >= this->size_ || row >= column_sizes_[col]) {
    throw std::out_of_range("Index out of range");
  }
  if ((*this)(col, row) != Marker::none) {
    throw std::invalid_argument("Position is not empty");
  }
  (*this)(col, row) = current_player_;
  if (current_player_ == Marker::red)
    current_player_ = Marker::blue;
  else current_player_ = Marker::red;
  return *this;
}

Marker Yboard::get_winner() {
  auto b = *this;
  for (auto subtractor = 1; subtractor < this->size_; subtractor++) {
    for (auto col = 0; col < (this->size_ - subtractor); col++) {
      for (auto row = 0; row < this->column_sizes_[col] - subtractor; row++) {
        if ((b(col,row+1) == b(col,row)) || (b(col+1,row) == b(col,row))) {
          // do nothing, since b(col,row) is already the desired value
        } else if (b(col,row+1) == b(col+1,row)) {
          b(col,row) = b(col,row+1);
        } else {
          b(col,row) = Marker::none;
        }
      }
    }
  }


  return b(0,0);
}

std::vector<std::pair<int,int> > Yboard::get_free_hexes() {
  std::vector<std::pair<int,int> > output;
  for (int col = 0; col < size_; col++) {
    for (int row = 0; row < column_sizes_[col]; row++) {
      if ( (*this)(col, row) == Marker::none ) {
        output.push_back(std::make_pair(col, row));
      }
    }
  }
  return output;
}

Yboard& Yboard::random_playout(bool quick=true) {
  std::random_device rd;
  auto rng = std::default_random_engine { rd() };
  auto get_free_hexes = this->get_free_hexes();
  std::shuffle(std::begin(get_free_hexes), std::end(get_free_hexes), rng);
  for (auto p : get_free_hexes) {
    if (!quick && (this->get_winner() != Marker::none)) {
      break;
    }
    this->move(p.first, p.second);
  }
  return *this;
}

Marker& Yboard::get_next_player() {
  return current_player_;
}

std::map<std::string, Marker> Yboard::get_dict() {
  std::map<std::string, Marker> result;
  for (auto col = 0; col < size_; col++) {
    for (auto row = 0; row < column_sizes_[col]; row++) {
      std::stringstream name;
      name << "cell" << col << "_" << row;
      result[name.str()] = (*this)(col,row);
    }
  }
  return result;
}

std::map<Marker, int> Yboard::random_playouts_won(const int num_playouts, bool quick=true) {
  std::map<Marker, int> result;
  result[Marker::red] = 0;
  result[Marker::blue] = 0;
  for (auto i=0; i < num_playouts; i++) {
    auto b = *this;
    auto winner = b.random_playout(quick).get_winner();
    result[winner] += 1;
  }
  return result;
}

std::vector<std::map<std::string, Marker>> Yboard::get_list_of_dicts(const int num_playouts, bool quick) {
  std::vector<std::map<std::string, Marker>> result;
  for (auto i=0; i < num_playouts; i++) {
    auto b = *this;
    auto winner = b.random_playout(quick).get_winner();
    auto b_dict = b.get_dict();
    b_dict["winner"] = winner;
    result.push_back(b_dict);
  }
  return result;
}

bool operator==(const Yboard& lhs, const Yboard& rhs) {
  return (
    (lhs.size_ == rhs.size_) &&
    (lhs.board_ == rhs.board_) &&
    (lhs.current_player_ == rhs.current_player_)
  );
}

PYBIND11_MODULE(_board, m) {
  py::enum_<Marker>(m, "Marker", R"doc(
  Enumeration for the possible contents of a hex

  Can be one of three values:  ``red``, corresponding to the integer ``1``; ``blue``, corresponding to the integer ``-1``; or ``none``, corresponding to the integer ``0``.
  )doc")
    .value("red", Marker::red)
    .value("blue", Marker::blue)
    .value("none", Marker::none)
    ;

  py::class_<Yboard>(m, "Yboard", R"doc(
    :param size: desired board size

    Implementation of the :py:class:`Board` protocol representing a Y board.  The constructor will create a board of ``size`` hexes on each side.
)doc")
    .def(py::init<const int>())
    .def("__str__", &Yboard::__str__)
    .def("move", &Yboard::move, ":meta private:")
    .def("get_free_hexes", &Yboard::get_free_hexes, ":meta private:")
    .def("get_winner", &Yboard::get_winner, ":meta private:")
    .def("get_next_player", &Yboard::get_next_player, ":meta private:")
    .def("random_playout", &Yboard::random_playout, ":meta private:", py::arg("quick") = true)
    .def("__copy__", [](const Yboard &self) {
      auto b = self;
      return b;
    })
    .def("__getitem__", [](const Yboard &self, py::tuple key) {
      auto col = key[0].cast<int>();
      auto row = key[1].cast<int>();
      return self(col, row);
    })
    .def("get_dict", &Yboard::get_dict, ":meta private:")
    .def("random_playouts_won", &Yboard::random_playouts_won, ":meta private:", py::arg("num_playouts"), py::arg("quick") = true)
    .def("get_list_of_dicts", &Yboard::get_list_of_dicts, ":meta private:", py::arg("num_playouts"), py::arg("quick") = true)
    .def(pybind11::self == pybind11::self)
    ;
}
