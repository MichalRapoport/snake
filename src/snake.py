import pygame
from constants import *


class Snake:
    def __init__(self, initial_position):
        self.body = [
            pygame.Rect(initial_position, (STEP_SIZE, STEP_SIZE))
        ]  # Snake starts with one segment at the initial position
        self.direction = (0, -STEP_SIZE)  # direction is initially set to move upwards
        self.ate_fruit = False
        self.score = 0
        self.speed = (
            SNAKE_SPEED  # speed controls how fast the snake moves (in seconds per step)
        )

    def move(self):
        new_head = self.body[0].move(
            self.direction
        )  # calculates the new head position by moving in the current direction
        if (  # Checks for wall collision/self-collision. If so, returns False for game over
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
        for i, segment in enumerate(self.body):
            colour = SNAKE_HEAD_COLOUR if i == 0 else SNAKE_COLOUR
            pygame.draw.rect(screen, colour, segment)

    def eat(self):
        self.ate_fruit = True
        self.score += 1

    def head(self):
        return self.body[0]

    """
    Set 1 step every snake.speed seconds.
    Therefore less milliseconds per step causes a faster speed.
    Alternatively, more milliseconds per step causes a slower speed.
    """

    def faster_speed(self):
        self.speed = max(0.1, self.speed - 0.1)

    def slower_speed(self):
        self.speed += 0.1
