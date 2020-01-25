# -*- coding: utf-8 -*-

from pygame import sprite
from pygame.surface import Surface

from constants import COLOR_GREEN, DIRECTION_Y_DOWN, DIRECTION_X_RIGHT, DIRECTION_Y_UP, DIRECTION_X_LEFT
from core import Arcanoid


class Ball(sprite.Sprite):
    def __init__(self, speed=None, scene: Arcanoid = None):
        super().__init__()
        self._scene = None
        self.scene = scene
        self.speed = speed or 2
        self.image = Surface((10, 10))
        self.image.fill(COLOR_GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (Arcanoid.SCREEN_WIDTH / 2, Arcanoid.SCREEN_WIDTH / 2)
        self.direction_y = DIRECTION_Y_DOWN
        self.direction_x = DIRECTION_X_RIGHT

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, scene: Arcanoid):
        self._scene = scene

    def _move_up(self):
        self.rect.y -= self.speed

    def _move_down(self):
        self.rect.y += self.speed

    def _move_left(self):
        self.rect.x -= self.speed

    def _move_right(self):
        self.rect.x += self.speed

    def toggle_direction(self):
        if self.rect.top <= 0:
            self.direction_y = DIRECTION_Y_DOWN
        elif self.rect.bottom >= Arcanoid.SCREEN_HEIGHT:
            self.direction_y = DIRECTION_Y_UP
        if self.rect.left <= 0:
            self.direction_x = DIRECTION_X_RIGHT
        elif self.rect.right >= Arcanoid.SCREEN_WIDTH:
            self.direction_x = DIRECTION_X_LEFT

    def move(self):
        if self.direction_y == DIRECTION_Y_DOWN:
            self._move_down()
        elif self.direction_y == DIRECTION_Y_UP:
            self._move_up()
        if self.direction_x == DIRECTION_X_RIGHT:
            self._move_right()
        elif self.direction_x == DIRECTION_X_LEFT:
            self._move_left()

    def update(self, *args):
        self.toggle_direction()
        self.move()
