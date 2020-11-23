# SNAKE by Norbert Kupeczki

import sys
import pygame
import random

# pip install pygame

pygame.init()
pygame.display.set_caption('Snake')
screen_width = 300
screen_height = 320
header_height = 20
screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
grey = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)

# Size and speed of the snake
snake_rect = 10
snake_speed = 10
clock = pygame.time.Clock()

game_over_font = pygame.font.SysFont("AgencyFB", 40)
end_game_text = pygame.font.SysFont("AgencyFB", 20)
score_font = pygame.font.SysFont("AgencyFB", 15)


class GameClass:
    food_x = 0.0
    food_y = 0.0
    snake_game_running = True
    playing_snake = True
    game_over = False
    snake_x = screen_width / 2
    snake_y = screen_height / 2
    snake_x_change = 0
    snake_y_change = 0
    snake_body = []
    snake_length = 1
    snake_head = []

    def __init__(self):
        print("Game successfully initialized")


def your_score(score):
    pygame.draw.rect(screen, black, [0, 0, screen_width, header_height])
    value = score_font.render("Score: " + str(score), True, white)
    screen.blit(value, [0, 0])


def draw_snake(snake_bl, snake_body_list):
    for x in snake_body_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_bl, snake_bl])
    snake_h = snake_body_list[len(snake_body_list) - 1]
    pygame.draw.rect(screen, black, [snake_h[0] + 2, snake_h[1] + 2, snake_bl - 4, snake_bl - 4])


def draw_apple():
    pygame.draw.rect(screen, red, [game.food_x + 1, game.food_y + 2, 3, 8])
    pygame.draw.rect(screen, red, [game.food_x + 6, game.food_y + 2, 3, 8])
    pygame.draw.rect(screen, red, [game.food_x, game.food_y + 3, 10, 5])
    pygame.draw.rect(screen, green, [game.food_x + 4, game.food_y, 2, 4])


def game_over_screen(score):
    screen.fill(black)
    game_over_text = game_over_font.render("Game Over!", True, red)
    screen.blit(game_over_text, [screen_width / 5, screen_height / 3.5])
    score_text = end_game_text.render("Your final score: " + str(score), True, yellow)
    screen.blit(score_text, [screen_width / 4, screen_height / 2])
    play_again = end_game_text.render("[P] - Play again, [Q] - Quit", True, red)
    screen.blit(play_again, [screen_width / 6, screen_height / 1.5])


def spawn_apple():
    legal_spawn = False
    apple_loc = [0, 0]
    while not legal_spawn:
        apple_loc[0] = round(random.randrange(0, screen_width - snake_rect) / 10.0) * 10.0
        apple_loc[1] = round(random.randrange(header_height, screen_height - snake_rect) / 10.0) * 10.0
        print(apple_loc)
        if game.snake_body:
            if apple_loc not in game.snake_body:
                legal_spawn = True
        else:
            legal_spawn = True

    game.food_x = apple_loc[0]
    game.food_y = apple_loc[1]


def init_game():
    game.snake_x = screen_width / 2
    game.snake_y = screen_height / 2
    game.snake_x_change = 0
    game.snake_y_change = 0
    game.snake_body = []
    game.snake_length = 1
    spawn_apple()
    game.playing_snake = True
    game.game_over = False


def input_event_handling():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and game.game_over:
                game.snake_game_running = False
                game.playing_snake = False
            elif event.key == pygame.K_p and game.game_over:
                game.game_over = False
                game.playing_snake = False
            elif event.key == pygame.K_LEFT:
                game.snake_x_change = -snake_rect
                game.snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                game.snake_x_change = snake_rect
                game.snake_y_change = 0
            elif event.key == pygame.K_UP:
                game.snake_y_change = -snake_rect
                game.snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                game.snake_y_change = snake_rect
                game.snake_x_change = 0


def move_snake():
    game.snake_x += game.snake_x_change
    game.snake_y += game.snake_y_change

    game.snake_head = [game.snake_x, game.snake_y]
    game.snake_body.append(game.snake_head)
    if len(game.snake_body) > game.snake_length:
        del game.snake_body[0]


def collision_check():
    collision_detected = False

    if game.snake_x >= screen_width or game.snake_x < 0 or game.snake_y >= screen_height or game.snake_y < header_height:
        collision_detected = True
    else:
        if game.snake_head in game.snake_body[:-1]:
            collision_detected = True

    return collision_detected


def apple_eaten_check():
    if game.snake_x == game.food_x and game.snake_y == game.food_y:
        spawn_apple()
        return 1
    else:
        return 0


def render_game():
    screen.fill(grey)
    draw_apple()
    draw_snake(snake_rect, game.snake_body)
    your_score(game.snake_length - 1)


def snake_game():
    while game.snake_game_running:
        init_game()
        print("Game starting")

        while game.playing_snake:
            input_event_handling()

            if game.game_over:
                game_over_screen(game.snake_length - 1)

            else:
                move_snake()
                game.game_over = collision_check()
                if not game.game_over:
                    game.snake_length += apple_eaten_check()
                    render_game()

            pygame.display.update()
            clock.tick(snake_speed)


if __name__ == '__main__':
    game = GameClass()
    snake_game()
    print("Thank you for playing, bye!")
    sys.exit(0)
