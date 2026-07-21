import pygame
import os
from game import Game
from grid import Grid
from snake import Direction, Snake
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from utils import handle_key_down

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
font = pygame.font.Font("PressStart2P-Regular.ttf", 24)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

game = Game()


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
                        handle_key_down(event, game)
    else:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                handle_key_down(event, game)

    # 2. update game state
    data = game.get_frame_meta_data()

    if not data.is_in_bounds or data.is_self_collision:
        break

    game.update_snake_pos(data.next_head_pos, data.will_eat)

    if data.will_eat:
        game.score += 1

    # 3. draw
    screen.fill("black")
    Grid.draw_score(screen, game.score, font)
    Grid.draw_food(screen, game.food_pos)
    Grid.draw_snake(screen, game.snake)

    pygame.display.flip()

pygame.quit()
