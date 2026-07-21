import pygame
from pygame.event import Event

from game import Game
from snake import Direction


def handle_key_down(event: Event, game: Game):
    if event.key == pygame.K_UP:
        game.snake.direction = Direction.UP
    elif event.key == pygame.K_DOWN:
        game.snake.direction = Direction.DOWN
    elif event.key == pygame.K_LEFT:
        game.snake.direction = Direction.LEFT
    elif event.key == pygame.K_RIGHT:
        game.snake.direction = Direction.RIGHT
