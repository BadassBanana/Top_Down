import pygame
import time
from player import *
from constant import *
import sys

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
backround_img = pygame.image.load("backround.png").convert()

class Backround(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(backround_img, (1600, 1200))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += -player.speedx
        self.rect.y += -player.speedy

backround = Backround()
backround_list.add(backround)