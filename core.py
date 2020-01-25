# -*- coding: utf-8 -*-
import pygame

from pygame import init as pygame_init
from pygame import quit as pygame_quit
from pygame import sprite, display
from pygame.time import Clock

from constants import COLOR_BLACK
from units import Ball


class Arcanoid:
    SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 320, 240
    FPS = 40
    __title__ = 'Арканоид 2020'

    def __init__(self):
        pygame_init()
        display.set_caption(Arcanoid.__title__)
        self.screen = display.set_mode(Arcanoid.SCREEN_SIZE)
        self.clock = Clock()
        self.game_sprites = sprite.Group()
        self.running = False

    def run(self):
        self.running = True
        self.game_sprites.add(Ball(scene=self))

        while self.running:
            self.clock.tick(Arcanoid.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.game_sprites.update()

            self.screen.fill(COLOR_BLACK)
            self.game_sprites.draw(self.screen)
            display.flip()

        pygame_quit()


if __name__ == '__main__':
    game = Arcanoid()
    game.run()
