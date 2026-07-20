import pygame
from game import Game
from grid import Grid
from snake import Direction, Snake
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

game = Game()

screen.fill("black")
Grid.draw_grid_lines(screen)

step_mode = False

while running:
    if step_mode:
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                    elif event.key == pygame.K_UP:
                        game.snake.direction = Direction.UP
                    elif event.key == pygame.K_DOWN:
                        game.snake.direction = Direction.DOWN
                    elif event.key == pygame.K_LEFT:
                        game.snake.direction = Direction.LEFT
                    elif event.key == pygame.K_RIGHT:
                        game.snake.direction = Direction.RIGHT
    else:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.snake.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    game.snake.direction = Direction.DOWN
                elif event.key == pygame.K_LEFT:
                    game.snake.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    game.snake.direction = Direction.RIGHT

    # 2. update game state
    data = game.get_frame_meta_data()

    if not data.is_in_bounds or data.is_self_collision:
        break

    game.update_snake_pos(data.next_head_pos, data.will_eat)

    if data.will_eat:
        Grid.clear_food(screen, data.original_food_pos)

    # 3. draw
    Grid.draw_food(screen, game.food_pos)
    Grid.draw_snake(screen, game.snake)

    pygame.display.flip()

pygame.quit()
