import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (34, 177, 76)
BLUE = (0, 0, 255)

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()