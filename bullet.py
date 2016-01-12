import pygame
from constant import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 0
        self.speedx = 0

        if player.direction == "left":
            self.speedx = -5

        if player.direction == "right":
            self.speedx = 5

        if player.direction == "up":
            self.speedy = -5

        if player.direction == "down":
            self.speedy = 5

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
