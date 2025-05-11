import pygame
import time
from fruit import fruit_image, fruit_size, getPosition
from constants import CAPTION, SNAKE_COLOUR, SNAKE_START_POSITION, KEY_TO_DIRECTION,WINDOW_SIZE, BACKGROUND_COLOUR

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption(CAPTION)

resized_fruit_image = pygame.transform.scale(fruit_image, fruit_size )
fruits = [getPosition()]
last_fruit_time = time.time()
snake_body = pygame.Rect(100,100, 30, 30)

run_game = True
while run_game:
    current_time = time.time()

    if current_time - last_fruit_time >= 5:
        fruits.append(getPosition())
        last_fruit_time = current_time

    screen.fill(BACKGROUND_COLOUR)  
    pygame.draw.rect(screen, SNAKE_COLOUR, snake_body)

    for fruit_position in fruits[:]:
        fruit_rect = pygame.Rect(fruit_position, fruit_size)
        if snake_body.colliderect(fruit_rect):
            fruits.remove(fruit_position)
        else:
            screen.blit(resized_fruit_image, fruit_position)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key in KEY_TO_DIRECTION:
              change_to, move_increment = KEY_TO_DIRECTION[event.key]
              snake_body = snake_body.move(move_increment)
              print("change_to -" , change_to)

        if event.type == pygame.QUIT:
            run_game = False

pygame.quit()
