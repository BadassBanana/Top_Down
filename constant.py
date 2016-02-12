import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (34, 177, 76)
BLUE = (0, 0, 255)

WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

all_sprites = pygame.sprite.Group()

player_bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()

enemy_sprites = pygame.sprite.Group()
#backround_list = pygame.sprite.Group()

tile_group = pygame.sprite.Group()
