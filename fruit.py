import random
import pygame
from constants import FRUIT_WIDTH, MAX_FRUIT_POSITION, MIN_FRUIT_POSITION
fruit_image = pygame.image.load("apple.jpg") 

fruit_size = (FRUIT_WIDTH, FRUIT_WIDTH)


def getPosition():
    return random.randint(MIN_FRUIT_POSITION, MAX_FRUIT_POSITION), random.randint(MIN_FRUIT_POSITION, MAX_FRUIT_POSITION)