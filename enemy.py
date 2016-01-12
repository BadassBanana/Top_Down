import pygame
import time
from constant import *
from spritesheet_functions import SpriteSheet
import sys

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Enemy(pygame.sprite.Sprite):
    # Sprite for the Player

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.walking_frames_d = [] # Images for animated walking.
        self.direction= ""

        sprite_sheet = SpriteSheet("enemy_spritesheet.png")

        for i in range(7):
            image = sprite_sheet.get_image((150 * i) + 40, 0, 54, 96)
            image.set_colorkey(DARK_GREEN)
            self.walking_frames_d.append(image)

        self.image = self.walking_frames_d[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

        self.last_update = pygame.time.get_ticks()
        self.frame = 0

        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        self.animate_sprite(self.walking_frames_d)
        self.check_bullets()

    def animate_sprite(self, anim_list):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.frame = (self.frame + 1) % 7
            self.image = anim_list[self.frame]

    def check_bullets(self):
        hits = pygame.sprite.groupcollide(enemy_sprites, bullets, True, True)
        for hit in hits:
            self.kill()

enemy = Enemy()
all_sprites.add(enemy)
enemy_sprites.add(enemy)
