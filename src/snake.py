import pygame
from constants import *


class Snake:
    def __init__(self, initial_position):
        self.body = [pygame.Rect(initial_position, (STEP_SIZE, STEP_SIZE))]
        self.direction = (0, -STEP_SIZE)
        self.ate_fruit = False
        self.score = 0
        self.speed = SNAKE_SPEED

    def move(self):
        new_head = self.body[0].move(self.direction)
        if (
            new_head.left < 0
            or new_head.right > WINDOW_SIZE
            or new_head.top < 0
            or new_head.bottom > WINDOW_SIZE + INFO_BAR_HEIGHT
        ):
            return False
        if new_head in self.body:
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
        self.score += 1

    def head(self):
        return self.body[0]

    def faster_speed(self):
        self.speed = max(0.1, self.speed - 0.1)

    def slower_speed(self):
        self.speed += 0.1
