from collection import namedtuple
import enum

#Player is basically just an enum
class Player(enum):
    black = 1
    white = 2

    @property 
    def other(self):
        return Player.black if self == Player.white else Player.white

#Point extends namedtuple.
#It's best to imagine it as a literal cartesian point (x,y)
#and when you call neighbors it returns a list of nearby points
class Point(namedtuple("Point", "row col")):
    def neighbors(self):
        return [
                Point(self.row - 1, self.col    ),
                Point(self.row + 1, self.col    ),
                Point(self.row    , self.col - 1),
                Point(self.row    , self.col + 1)
                ]


