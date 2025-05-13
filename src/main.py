import pygame
import time
from snake import Snake
from fruit import *
from constants import *


def init_game():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + INFO_BAR_HEIGHT))
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


def display_info_bar(start_time, snake, screen):
    elapsed_time = int(time.time() - start_time)
    pygame.draw.rect(
        screen, pygame.Color("black"), (0, 0, WINDOW_SIZE, INFO_BAR_HEIGHT)
    )
    font = pygame.font.Font("assets/game_font.ttf", 24)
    time_text = font.render(f"Time: {elapsed_time}s", True, TEXT_COLOUR)
    score_text = font.render(f"Score: {snake.score}", True, TEXT_COLOUR)

    speed_text = font.render(f"Speed: {snake.speed:.2f}s", True, TEXT_COLOUR)
    screen.blit(speed_text, (WINDOW_SIZE // 2 - speed_text.get_width() // 2, 10))
    screen.blit(time_text, (10, 10))
    screen.blit(score_text, (WINDOW_SIZE - score_text.get_width() - 10, 10))


def run_game():
    screen = init_game()
    snake = Snake((WINDOW_SIZE * 2 // 3, WINDOW_SIZE * 2 // 3))
    fruits = [generate_fruit_position()]

    last_fruit_time = time.time()
    last_move_time = time.time()
    start_time = time.time()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # if user presses a directional key, switch snake's direction
                if event.key in KEY_TO_DIRECTION:
                    change_to, move_dir = KEY_TO_DIRECTION[event.key]
                    snake.direction = move_dir
                # if user presses + or -, change snake's speed accordingly
                elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                    snake.faster_speed()

                elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    snake.slower_speed()

            if event.type == pygame.QUIT:
                running = False

        if (
            time.time() - last_fruit_time >= FRUIT_CREATION_TIME
        ):  # generate a fruit every FRUIT_CREATION_TIME
            fruits.append(generate_fruit_position())
            last_fruit_time = time.time()

        if (
            time.time() - last_move_time >= snake.speed
        ):  # move snake's location every snake.speed seconds
            is_alive = snake.move()
            if not is_alive:
                end_game(screen, snake.score)
                running = False
            last_move_time = time.time()

        screen.fill(BACKGROUND_COLOUR)
        snake.draw(screen)
        display_info_bar(start_time, snake, screen)

        for fruit_position in fruits[:]:  # check if the snake ate a fruit
            head = snake.head()
            fruit_rect = pygame.Rect(fruit_position, fruit_size)
            if head.colliderect(fruit_rect):
                fruits.remove(fruit_position)
                snake.eat()
            else:
                screen.blit(resized_fruit_image, fruit_position)

        pygame.display.flip()  # update entire screen changes


pygame.quit()

if __name__ == "__main__":
    run_game()
