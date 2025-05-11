import pygame
import time
from fruit import resized_fruit_image, fruit_size, getPosition
from constants import SNAKE_SPEED,FRUIT_CREATION_TIME,CAPTION, SNAKE_COLOUR, KEY_TO_DIRECTION, WINDOW_SIZE, BACKGROUND_COLOUR

def init_game():
  pygame.init()
  screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
  pygame.display.set_caption(CAPTION)
  return screen

def draw_snake(screen, snake_body):
  for segment in snake_body:
    pygame.draw.rect(screen, SNAKE_COLOUR, segment)

fruits = [getPosition()]
ate_fruit = False
last_fruit_time = time.time()
snake_body = [pygame.Rect(500, 500, 30, 30)]  
current_direction = (0, 0)
last_move_time = time.time() 
screen = init_game()

run_game = True
while run_game:
    current_time = time.time()

    if current_time - last_fruit_time >= FRUIT_CREATION_TIME:
        fruits.append(getPosition())
        last_fruit_time = current_time

    if current_time - last_move_time >= SNAKE_SPEED:
        new_head = snake_body[0].move(current_direction)
        snake_body.insert(0, new_head)

        if not ate_fruit:
            snake_body.pop()  

        ate_fruit = False
        last_move_time = current_time

    screen.fill(BACKGROUND_COLOUR)

    draw_snake(screen, snake_body)

    for fruit_position in fruits[:]:
        fruit_rect = pygame.Rect(fruit_position, fruit_size)
        if snake_body[0].colliderect(fruit_rect):
            fruits.remove(fruit_position)
            ate_fruit = True
        else:
            screen.blit(resized_fruit_image, fruit_position)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in KEY_TO_DIRECTION:
                change_to, move_increment = KEY_TO_DIRECTION[event.key]
                current_direction = move_increment

        if event.type == pygame.QUIT:
            run_game = False

pygame.quit()
