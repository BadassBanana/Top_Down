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

class Player(pygame.sprite.Sprite):
    # Sprite for the Player

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.walking_frames_d = [] # Images for animated walking.
        self.walking_frames_u = []
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.direction= ""

        sprite_sheet = SpriteSheet("spritesheet.png")

        for i in range(7):
            image = sprite_sheet.get_image((150 * i) + 40, 22, 54, 96)
            image.set_colorkey(DARK_GREEN)
            self.walking_frames_d.append(image)

        for i in range(7):
            image = sprite_sheet.get_image((150 * i) + 40, 125, 54, 109)
            image.set_colorkey(DARK_GREEN)
            self.walking_frames_u.append(image)

        for i in range(7):
            image = sprite_sheet.get_image((150 * i) + 20, 257, 81, 94)
            image.set_colorkey(DARK_GREEN)
            self.walking_frames_l.append(image)

        for i in range(7):
            image = sprite_sheet.get_image((150 * i) + 33, 375, 80, 92)
            image.set_colorkey(DARK_GREEN)
            self.walking_frames_r.append(image)

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
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -2
            self.animate_sprite(self.walking_frames_u)
            self.direction = "up"
        if keystate[pygame.K_DOWN]:
            self.speedy = 2
            self.animate_sprite(self.walking_frames_d)
            self.direction = "down"
        if keystate[pygame.K_LEFT]:
            self.speedx = -2
            self.animate_sprite(self.walking_frames_l)
            self.direction = "left"
        if keystate[pygame.K_RIGHT]:
            self.speedx = 2
            self.animate_sprite(self.walking_frames_r)
            self.direction = "right"

        if keystate[pygame.K_SPACE]:
            self.shoot()

        self.rect.y += self.speedy
        self.rect.x += self.speedx

    def animate_sprite(self, anim_list):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.frame = (self.frame + 1) % 7
            self.image = anim_list[self.frame]

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.centery + 25)
            all_sprites.add(bullet)
            bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = 0
        self.speedy = 0

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
        self.rect.x += self.speedx
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0 or self.rect.top> HEIGHT:
            self.kill()
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.kill()

player = Player()
all_sprites.add(player)

