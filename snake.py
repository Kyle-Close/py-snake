from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Snake:
    def __init__(self):
        self.size = 1
        self.direction = Direction.RIGHT
        self.pos_stack = [(0, 0)]
        self.prev_tail_pos = ()

    def move_snake(self, did_eat: bool):
        if did_eat:
            new_head = self.calc_next_coords(self.pos_stack[-1])
            self.pos_stack.append(new_head)
            return

        top = self.pos_stack.pop()
        head = top if len(self.pos_stack) == 0 else self.pos_stack[-1]

        self.pos_stack.append(self.calc_next_coords(head))

        self.prev_tail_pos = top

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
