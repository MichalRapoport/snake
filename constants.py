import pygame

WINDOW_SIZE = 700
BACKGROUND_COLOUR = (255, 255, 255)
CAPTION = "Snake game"
FRUIT_WIDTH = 30
MIN_FRUIT_POSITION = FRUIT_WIDTH
MAX_FRUIT_POSITION = WINDOW_SIZE - FRUIT_WIDTH



SNAKE_START_POSITION = (100, 100)
STEP_SIZE = 30
SNAKE_COLOUR = (10, 128, 1) 

DIRECTIONS = {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "right": pygame.K_RIGHT,
    "left": pygame.K_LEFT
}
KEY_TO_DIRECTION = {
    DIRECTIONS["up"]:  ('UP', (0, -STEP_SIZE)),
    DIRECTIONS["down"]: ('DOWN', (0, STEP_SIZE)), 
    DIRECTIONS["left"]: ('LEFT', (-STEP_SIZE, 0)), 
    DIRECTIONS["right"]: ('RIGHT', (STEP_SIZE, 0))  
}
