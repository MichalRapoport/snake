import pygame

from fruit import fruit_image, fruit_size, getPosition
from constants import WINDOW_SIZE, BACKGROUND_COLOUR

pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Snake game")

resized_fruit_image = pygame.transform.scale(fruit_image, fruit_size )
fruit_init_position = getPosition()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOUR)  
    screen.blit(resized_fruit_image, fruit_init_position) 
    pygame.display.flip()

pygame.quit()
