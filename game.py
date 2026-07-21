import pygame
from constants import GRID_COLS, GRID_ROWS
from snake import Snake
from random import randrange
from dataclasses import dataclass


@dataclass
class FrameMetaData:
    next_head_pos: tuple[int, int]
    will_eat: bool
    original_food_pos: tuple[int, int]
    is_in_bounds: bool
    is_self_collision: bool


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food_pos = self.get_new_food_pos()
        self.score = 0

    def get_frame_meta_data(self) -> FrameMetaData:
        next_head_pos = self.snake.calc_next_coords(self.snake.pos_stack[-1])
        will_eat = next_head_pos == self.food_pos
        original_food_pos = self.food_pos
        is_in_bounds = self.is_in_bounds(next_head_pos)
        is_self_collision = self.is_self_collision(next_head_pos)

        return FrameMetaData(next_head_pos, will_eat, original_food_pos, is_in_bounds, is_self_collision)

    def update_snake_pos(self, next_head_pos: tuple[int, int], did_eat: bool):
        if did_eat:
            self.snake.pos_stack.append(next_head_pos)
            self.food_pos = self.get_new_food_pos()
            self.snake.prev_tail_pos = None
        else:
            tail = self.snake.pos_stack.pop(0)
            self.snake.pos_stack.append(next_head_pos)
            self.snake.prev_tail_pos = tail

    def get_new_food_pos(self):
        x = randrange(GRID_COLS)
        y = randrange(GRID_ROWS)
        return (x, y)

    def is_in_bounds(self, pos: tuple[int, int]):
        if pos[0] < 0 or pos[0] >= GRID_COLS:
            return False
        if pos[1] < 0 or pos[1] >= GRID_ROWS:
            return False

        return True

    def is_self_collision(self, next_head_pos: tuple[int, int]):
        if next_head_pos in self.snake.pos_stack:
            return True
        return False
