import pygame
from grid import Grid
from snake import Direction, Snake
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

snake = Snake()

screen.fill("black")
Grid.draw_grid_lines(screen)

while running:
    # 1. handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Direction.UP
            elif event.key == pygame.K_DOWN:
                snake.direction = Direction.DOWN
            elif event.key == pygame.K_LEFT:
                snake.direction = Direction.LEFT
            elif event.key == pygame.K_RIGHT:
                snake.direction = Direction.RIGHT

    # 2. update game state
    snake.move_snake(True)

    # 3. draw
    Grid.draw_food(screen, 10, 10)
    Grid.draw_snake(screen, snake)

    pygame.display.flip()

    clock.tick(10)  # cap at 60 FPS

pygame.quit()
