from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_COLS, GRID_ROWS, FOOD_HEIGHT, FOOD_WIDTH
import pygame

from snake import Snake


class Grid:
    def __init__(self):
        pass

    @staticmethod
    def draw_grid_lines(screen):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

        # draw grid column lines
        for i in range(int(SCREEN_WIDTH / GRID_COLS), SCREEN_WIDTH, int(SCREEN_WIDTH / GRID_COLS)):
            pygame.draw.line(overlay, (255, 255, 255, 128), (i, 0), (i, SCREEN_HEIGHT))

        # draw grid row lines
        for i in range(int(SCREEN_HEIGHT / GRID_ROWS), SCREEN_HEIGHT, int(SCREEN_HEIGHT / GRID_ROWS)):
            pygame.draw.line(overlay, (255, 255, 255, 128), (0, i), (SCREEN_WIDTH, i))

        screen.blit(overlay, (0, 0))

    @staticmethod
    def draw_food(screen, pos: tuple[int, int]):
        x = pos[0] * (SCREEN_WIDTH // GRID_COLS) + (SCREEN_WIDTH // GRID_COLS // 4)
        y = pos[1] * (SCREEN_HEIGHT // GRID_ROWS) + (SCREEN_HEIGHT // GRID_ROWS // 4)
        food = pygame.Rect(x, y, FOOD_WIDTH, FOOD_HEIGHT)
        pygame.draw.rect(screen, "green", food)

    @staticmethod
    def clear_food(screen, pos: tuple[int, int]):
        x = pos[0] * (SCREEN_WIDTH // GRID_COLS) + (SCREEN_WIDTH // GRID_COLS // 4)
        y = pos[1] * (SCREEN_HEIGHT // GRID_ROWS) + (SCREEN_HEIGHT // GRID_ROWS // 4)
        pygame.draw.rect(screen, "black", pygame.Rect(x, y, FOOD_WIDTH, FOOD_HEIGHT))

    @staticmethod
    def draw_snake(screen, snake: Snake):
        if snake.prev_tail_pos:
            x = snake.prev_tail_pos[0] * (SCREEN_WIDTH // GRID_COLS) + ((SCREEN_WIDTH // GRID_COLS) // 2)
            y = snake.prev_tail_pos[1] * (SCREEN_HEIGHT // GRID_ROWS) + ((SCREEN_HEIGHT // GRID_ROWS) // 2)
            size = SCREEN_HEIGHT // GRID_ROWS // 3
            pygame.draw.circle(screen, "black", (x, y), size)

        for pos in snake.pos_stack:
            x = (pos[0] * (SCREEN_WIDTH // GRID_COLS)) + ((SCREEN_WIDTH // GRID_COLS) // 2)
            y = pos[1] * (SCREEN_HEIGHT // GRID_ROWS) + ((SCREEN_HEIGHT // GRID_ROWS) // 2)
            size = SCREEN_HEIGHT // GRID_ROWS // 3
            pygame.draw.circle(screen, "red", (x, y), size)
