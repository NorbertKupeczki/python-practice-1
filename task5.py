import sys
import pygame
import random

pygame.init()
pygame.display.set_caption('Snake')

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
grey = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)

snake_block = 10
snake_speed = 10
clock = pygame.time.Clock()

game_over_font = pygame.font.SysFont("bahnschrift", 40)
end_game_text = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 15)

screen_width = 300
screen_height = 320
header_height = 20
screen = pygame.display.set_mode((screen_width, screen_height))

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


def your_score(score):
    pygame.draw.rect(screen, black, [0, 0, screen_width, header_height])
    value = score_font.render("Score: " + str(score), True, white)
    screen.blit(value, [0, 0])


def draw_snake(snake_bl, snake_body_list):
    for x in snake_body_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_bl, snake_bl])
    snake_h = snake_body_list[len(snake_body_list) - 1]
    pygame.draw.rect(screen, black, [snake_h[0] + 2, snake_h[1] + 2, snake_bl - 4, snake_bl - 4])


def game_over_screen(score):
    screen.fill(black)
    game_over_text = game_over_font.render("Game Over!", True, red)
    screen.blit(game_over_text, [screen_width / 5, screen_height / 3.5])
    score_text = end_game_text.render("Your final score: " + str(score), True, yellow)
    screen.blit(score_text, [screen_width / 4, screen_height / 2])
    play_again = end_game_text.render("[P] - Play again, [Q] - Quit", True, red)
    screen.blit(play_again, [screen_width / 6, screen_height / 1.5])


def spawn_apple():
    global food_x
    global food_y
    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(header_height, screen_height - snake_block) / 10.0) * 10.0


def init_game():
    global snake_x, snake_y, snake_x_change, snake_y_change, snake_body, snake_length, playing_snake, game_over

    snake_x = screen_width / 2
    snake_y = screen_height / 2
    snake_x_change = 0
    snake_y_change = 0
    snake_body = []
    snake_length = 1
    spawn_apple()
    playing_snake = True
    game_over = False


def input_event_handling():
    global game_over, playing_snake, snake_game_running
    global snake_x_change, snake_y_change

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and game_over:
                snake_game_running = False
                playing_snake = False
            elif event.key == pygame.K_p and game_over:
                game_over = False
                playing_snake = False
            elif event.key == pygame.K_LEFT:
                snake_x_change = -snake_block
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block
                snake_x_change = 0


def move_snake():
    global snake_x, snake_y, snake_head, snake_body

    snake_x += snake_x_change
    snake_y += snake_y_change

    snake_head = [snake_x, snake_y]
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]


def collision_check():
    collision_detected = False

    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < header_height:
        collision_detected = True
    else:
        for body in snake_body[:-1]:
            if body == snake_head:
                collision_detected = True

    return collision_detected


def apple_eaten_check():
    if snake_x == food_x and snake_y == food_y:
        spawn_apple()
        return 1
    else:
        return 0


def render_game():
    screen.fill(grey)
    pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
    draw_snake(snake_block, snake_body)
    your_score(snake_length - 1)


def snake_game():
    global food_x, food_y, snake_x, snake_y, snake_x_change, snake_y_change
    global playing_snake, game_over, snake_game_running, snake_length

    while snake_game_running:
        init_game()
        print("Game starting")

        while playing_snake:
            input_event_handling()

            if game_over:
                game_over_screen(snake_length - 1)

            else:
                move_snake()
                game_over = collision_check()
                if not game_over:
                    snake_length += apple_eaten_check()
                    render_game()

            pygame.display.update()
            clock.tick(snake_speed)


if __name__ == '__main__':
    snake_game()
    print("Thank you for playing, bye!")
    sys.exit(0)
