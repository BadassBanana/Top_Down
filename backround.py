import pygame
import time
from player import *
from constant import *
import sys

img = pygame.image.load("grass.png").convert()
floor_one = pygame.image.load("floor_one.bmp").convert()
wall_bottom = pygame.image.load("wall_bottom.bmp").convert()
wall_right = pygame.image.load("wall_right.bmp").convert()
wall_top = pygame.image.load("wall_top.bmp").convert()
wall_left =pygame.image.load("wall_left.bmp").convert()

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, is_solid):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.solid_state = is_solid

    def update(self):
        self.rect.x += -player.speedx
        self.rect.y += -player.speedy




level_one = [[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
            [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5],
            [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5],
            [5,1,1,1,3,2,2,2,2,2,2,2,2,2,5,1,1,3,2,2,2,2,2,2,2,2,2,1,1,1,5],
            [5,1,1,1,3,1,1,1,1,1,1,1,1,1,5,1,1,3,1,1,1,1,1,1,1,1,5,1,1,1,5],
            [5,1,1,1,3,1,1,1,1,1,1,1,1,1,5,1,1,3,1,1,1,1,1,1,1,1,5,1,1,1,5],
            [5,1,1,1,3,1,1,1,1,1,1,1,1,1,5,1,1,3,1,1,1,1,1,1,1,1,5,1,1,1,5],
            [5,1,1,1,3,1,1,1,1,1,1,1,1,1,5,1,1,3,1,1,1,1,1,1,1,1,5,1,1,1,5],
            [5,1,1,1,3,1,1,1,1,1,1,1,1,1,5,1,1,3,1,1,1,1,1,1,1,1,5,1,1,1,5],
            [5,1,1,1,3,1,1,1,1,1,1,1,1,1,5,1,1,3,1,1,1,1,1,1,1,1,5,1,1,1,5],
            [5,1,1,1,3,1,1,1,1,1,1,1,1,1,5,1,1,3,1,1,1,1,1,1,1,1,5,1,1,1,5],
            [5,1,1,1,3,1,1,1,1,1,1,1,1,1,5,1,1,3,1,1,1,1,1,1,1,1,5,1,1,1,5],
            [5,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,5],
            [5,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,5],
            [5,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,5],
            [5,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,5],
            [5,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,5],
            [5,1,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,5],
            [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5],
            [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5],
            [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5],
            [5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,5],
            [5,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [5,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [5,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [5,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [5,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [5,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [5,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [5,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [5,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]

for y, row in enumerate(level_one):
    for x, terrain_num in enumerate(row):
        if terrain_num == 0:
            None

        elif terrain_num == 1:
            tile = Tile(floor_one, False)
            tile.rect.center = (x * 64, y * 64)
            tile_group.add(tile)

        elif terrain_num == 2:
            tile = Tile(wall_bottom, True)
            tile.rect.center = (x * 64, y * 64)
            tile_group.add(tile)

        elif terrain_num == 3:
            tile = Tile(wall_right, True)
            tile.rect.center = (x * 64, y * 64)
            tile_group.add(tile)

        elif terrain_num == 4:
            tile = Tile(wall_top, True)
            tile.rect.center = (x * 64, y * 64)
            tile_group.add(tile)

        elif terrain_num == 5:
            tile = Tile(wall_left, True)
            tile.rect.center = (x * 64, y * 64)
            tile_group.add(tile)

#for y in range(40):
#    for x in range(40):
#        tile = Tile(img)
#        tile.rect.center = (x * 70, y * 70)
#        tile_group.add(tile)


#backround_img = pygame.image.load("backround.png").convert()

#class Backround(pygame.sprite.Sprite):
#    def __init__(self):
#        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.transform.scale(backround_img, (6400, 4800))
#        self.rect = self.image.get_rect()

#    def update(self):
#        self.rect.x += -player.speedx
#        self.rect.y += -player.speedy


#backround = Backround()
#backround_list.add(backround)