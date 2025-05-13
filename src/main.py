import pygame
import time
from snake import Snake
from fruit import *
from constants import *


def init_game():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption(CAPTION)
    return screen


def end_game(screen, score):
    screen.fill(BACKGROUND_COLOUR)
    score_font = pygame.font.Font("assets/game_font.ttf", 30)
    score_message = score_font.render(f"Score: {score}", True, TEXT_COLOUR)
    screen.blit(
        score_message,
        (WINDOW_SIZE // 2 - score_message.get_width() // 2, WINDOW_SIZE // 2 + 50),
    )
    screen.blit(GAME_OVER_MESSAGE, GAME_OVER_BOX)
    pygame.display.flip()
    pygame.time.wait(3000)


def draw_fruits(screen, fruits):
    for fruit in fruits:
        screen.blit(resized_fruit_image, fruit)


def check_collisions(snake, fruits):
    head = snake.head()
    for fruit in fruits[:]:
        fruit_rect = pygame.Rect(fruit, fruit_size)
        if head.colliderect(fruit_rect):
            snake.eat()
            fruits.remove(fruit)


def run_game():
    screen = init_game()
    snake = Snake((500, 500))
    fruits = [generate_fruit_position()]

    last_fruit_time = time.time()
    last_move_time = time.time()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key in KEY_TO_DIRECTION:
                change_to, move_dir = KEY_TO_DIRECTION[event.key]
                snake.direction = move_dir

            if event.type == pygame.QUIT:
                running = False

        if time.time() - last_fruit_time >= FRUIT_CREATION_TIME:
            fruits.append(generate_fruit_position())
            last_fruit_time = time.time()

        if time.time() - last_move_time >= SNAKE_SPEED:
            is_alive = snake.move()
            if not is_alive:
                end_game(screen, snake.score)
                running = False
            last_move_time = time.time()

        screen.fill(BACKGROUND_COLOUR)
        snake.draw(screen)

        for fruit_position in fruits[:]:
            head = snake.head()
            fruit_rect = pygame.Rect(fruit_position, fruit_size)
            if head.colliderect(fruit_rect):
                fruits.remove(fruit_position)
                snake.eat()
            else:
                screen.blit(resized_fruit_image, fruit_position)

        pygame.display.flip()


pygame.quit()

if __name__ == "__main__":
    run_game()
