import pygame
from grid import Grid
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, FOOD_WIDTH, FOOD_HEIGHT

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # 1. handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and pygame.K_UP:
            pass
            # move snake up on next frame

    # 2. update game state (nothing yet)

    # 3. draw
    screen.fill("black")
    Grid.draw_grid_lines(screen)

    Grid.draw_food(screen, 10, 10)
    Grid.draw_snake(screen, 4, 4)

    pygame.display.flip()

    clock.tick(60)  # cap at 60 FPS

pygame.quit()
