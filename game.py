from constants import GRID_COLS, GRID_ROWS
from snake import Snake
from random import randrange


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food_pos = self.get_new_food_pos()
        self.score = 0

    def update_snake_pos(self):
        next_head_pos = self.snake.calc_next_coords(self.snake.pos_stack[-1])

        if next_head_pos == self.food_pos:
            self.snake.pos_stack.append(next_head_pos)
            self.food_pos = self.get_new_food_pos()
            self.snake.prev_tail_pos = None
            return True

        tail = self.snake.pos_stack.pop(0)

        self.snake.pos_stack.append(next_head_pos)
        self.snake.prev_tail_pos = tail

        return False

    def get_new_food_pos(self):
        x = randrange(GRID_COLS)
        y = randrange(GRID_ROWS)
        return (x, y)
