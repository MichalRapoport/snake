import pygame
from constants import SNAKE_COLOUR, STEP_SIZE, WINDOW_SIZE


class Snake:
    def __init__(self, initial_position):
        self.body = [pygame.Rect(initial_position, (STEP_SIZE, STEP_SIZE))]
        self.direction = (0, 0)
        self.ate_fruit = False

    def move(self):
        new_head = self.body[0].move(self.direction)
        if (
            new_head.left < 0
            or new_head.right > WINDOW_SIZE
            or new_head.top < 0
            or new_head.bottom > WINDOW_SIZE
        ):
            return False

        self.body.insert(0, new_head)
        if not self.ate_fruit:
            self.body.pop()
        else:
            self.ate_fruit = False
        return True

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, SNAKE_COLOUR, segment)

    def eat(self):
        self.ate_fruit = True

    def head(self):
        return self.body[0]
