import random
import pygame
from constants import FRUIT_WIDTH, MAX_FRUIT_POSITION, MIN_FRUIT_POSITION

fruit_image = pygame.image.load("assets/fruit.jpg")
fruit_size = (FRUIT_WIDTH, FRUIT_WIDTH)
resized_fruit_image = pygame.transform.scale(fruit_image, fruit_size)


def generate_fruit_position():
    return random.randint(MIN_FRUIT_POSITION, MAX_FRUIT_POSITION), random.randint(
        MIN_FRUIT_POSITION, MAX_FRUIT_POSITION
    )
