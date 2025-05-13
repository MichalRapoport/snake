import pygame

WINDOW_SIZE = 700
BACKGROUND_COLOUR = (255, 255, 255)
CAPTION = "Snake game"
INFO_BAR_HEIGHT = 40

pygame.font.init()
GAME_OVER_FONT = pygame.font.Font("assets/game_font.ttf", 60)
TEXT_COLOUR = (255, 0, 0)
GAME_OVER_MESSAGE = GAME_OVER_FONT.render("Game Over", True, TEXT_COLOUR)
GAME_OVER_BOX = GAME_OVER_MESSAGE.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))

FRUIT_WIDTH = 30
MIN_FRUIT_POSITION = FRUIT_WIDTH
MAX_FRUIT_POSITION = WINDOW_SIZE - FRUIT_WIDTH
FRUIT_CREATION_TIME = 5  # every 5 seconds, a new fruit will be generated

STEP_SIZE = 30
SNAKE_COLOUR = (10, 128, 1)
SNAKE_SPEED = 0.5  # every 0.5 seconds, move the snake

DIRECTIONS = {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "right": pygame.K_RIGHT,
    "left": pygame.K_LEFT,
}
KEY_TO_DIRECTION = {
    DIRECTIONS["up"]: ("UP", (0, -STEP_SIZE)),
    DIRECTIONS["down"]: ("DOWN", (0, STEP_SIZE)),
    DIRECTIONS["left"]: ("LEFT", (-STEP_SIZE, 0)),
    DIRECTIONS["right"]: ("RIGHT", (STEP_SIZE, 0)),
}
