from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Snake:
    def __init__(self):
        self.direction = Direction.RIGHT
        self.pos_stack = [(0, 0)]
        self.prev_tail_pos: None | tuple[int, int] = None

    def calc_next_coords(self, curr_coords: tuple[int, int]):
        match self.direction:
            case Direction.UP:
                return (curr_coords[0], curr_coords[1] - 1)
            case Direction.DOWN:
                return (curr_coords[0], curr_coords[1] + 1)
            case Direction.LEFT:
                return (curr_coords[0] - 1, curr_coords[1])
            case Direction.RIGHT:
                return (curr_coords[0] + 1, curr_coords[1])
