import copy
from dlgo.gotypes import Player

# collection of class methods for generating moves
# moves really just keep track of what move is done
# i.e. a point, a play etc
# not that placing a point (stone) is a play
# so we set play to be true. This is the only data not passed in the constructor
class Move():
    def __init__(self, point=None, is_pass=False, is_resign=False):
        assert (point is not None) ^ is_pass ^ is_resign
        self.point     = point
        self.is_play   = (self.point is not None) 
        self.is_pass   = is_pass 
        self.is_resign = is_resign
        
    @classmethod 
    def play(cls, point):
        return Move(point = point)

    @classmethod 
    def pass_turn(cls):
        return Move(is_pass = True)

    @classmethod
    def resign(cls):
        return Move(is_resign = True)

# GoString class keeps track of groups of stones
# And, for simplicity, the liberties of a given group

class GoString():
    def __init__(self, color , stones, liberties):
        self.color     = color
        self.stones    = set(stones)
        self.liberties = set(liberties)

    def remove_liberty(self, point):
        self.liberties.remove(point)

    def add_liberty(self, point):
        self.liberties.add(point)

    def merged_with(self, go_string):
        assert go_string.color == self.color
        combined_stones = self.stones | go_string.stones
        return GoString(
                self.color,
                combined_stones,
                (self.liberties | go_string.liberties) - combined_stones
                )

    @property
    def num_liberties(self):
        return len(self.liberties)

    def __eq__(self, other):
        return isinstance(other, GoString) and \
                self.color = other.color and \
                self.stones == other.stones and \
                self.liberties == other.liberties

class Board():
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols

    def place_stone(self, player, point):
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None
        adjacent_same_color = []
        adjacent_opposite_color = []
        for neighbor in point.neighbors():
            if not self.is_on_grid(neighbor):
                continue
            neighbor_string = self._grid.get(neighbor)
            if neighbor_string is None:
                liberties.append(neighbor)
            elif neighbor_string.color == player:
                if neighbor_string not in adjacent_same_color:
                    adjacent_opposite_color,.append(neighbor_string)
            else:
                if neighbor_string not in adjacent_opposite_color:
                    adjacent_opposite_color.append(neighbor_string)

        new_string = GoString(player, [point], liberties)
