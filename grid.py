from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_COLS, GRID_ROWS, FOOD_HEIGHT, FOOD_WIDTH
import pygame


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
    def draw_food(screen, x: int, y: int):
        x = x * (SCREEN_WIDTH // GRID_COLS)
        y = y * (SCREEN_HEIGHT // GRID_ROWS)
        food = pygame.Rect(x, y, FOOD_WIDTH, FOOD_HEIGHT)
        pygame.draw.rect(screen, "green", food)

    @staticmethod
    def draw_snake(screen, x: int, y: int):
        x = (x * (SCREEN_WIDTH // GRID_COLS)) + ((SCREEN_WIDTH // GRID_COLS) // 2)
        y = y * (SCREEN_HEIGHT // GRID_ROWS) + ((SCREEN_HEIGHT // GRID_ROWS) // 2)
        size = SCREEN_HEIGHT // GRID_ROWS // 2
        pygame.draw.circle(screen, "red", (x, y), size)
