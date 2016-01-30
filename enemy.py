import pygame
import time
from player import *
from constant import *
from spritesheet_functions import SpriteSheet
import sys
import math

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Enemy(pygame.sprite.Sprite):
    # Sprite for the Player

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.walking_frames_d = [] # Images for animated walking.
        self.walking_frames_u = []
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.direction= ""

        sprite_sheet = SpriteSheet("enemy_spritesheet.png")

        for i in range(7):
            image = sprite_sheet.get_image((150 * i) + 40, 0, 54, 96)
            image.set_colorkey(DARK_GREEN)
            self.walking_frames_d.append(image)

        for i in range(7):
            image = sprite_sheet.get_image((150 * i) + 40, 120, 54, 82)
            image.set_colorkey(DARK_GREEN)
            self.walking_frames_u.append(image)

        for i in range(7):
            image = sprite_sheet.get_image((150 * i) + 40, 235, 61, 82)
            image.set_colorkey(DARK_GREEN)
            self.walking_frames_l.append(image)

        for i in range(7):
            image = sprite_sheet.get_image((150 * i) + 40, 352, 60, 80)
            image.set_colorkey(DARK_GREEN)
            self.walking_frames_r.append(image)


        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y) # 120, 200
        self.speedx = -2
        self.speedy = -2

        self.last_update = pygame.time.get_ticks()

        self.frame = 0
        self.frames = self.walking_frames_d

        self.shoot_delay = 500

        self.last_shot = pygame.time.get_ticks()

    def update(self):
        self.animate_sprite(self.frames)
        self.check_bullets()
        self.scrolling()
        self.move_towards_player(player)
        self.check_direction()

        if self.rect.x >= player.rect.x - 50 or self.rect.x <= player.rect.x + 50:
            self.shoot()

        if self.rect.y >= player.rect.y - 50 or self.rect.y <= player.rect.y + 50:
            self.shoot()

    def animate_sprite(self, anim_list):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.frame = (self.frame + 1) % 7
            self.image = anim_list[self.frame]

    def check_bullets(self):
        hits = pygame.sprite.groupcollide(enemy_sprites, player_bullets, True, True)
        for hit in hits:
            self.kill()

    def scrolling(self):
        self.rect.x += -player.speedx
        self.rect.y += -player.speedy

    def move_towards_player(self, player):
        # find normalized direction vector (dx, dy) between enemy and player
        self.dx = self.rect.x - player.rect.x
        self.dy = self.rect.y - player.rect.y
        dist = math.hypot(self.dx, self.dy)

        try:
            self.dx = self.dx /dist
            self.dy = self.dy / dist
        except ZeroDivisionError:
            dist = 1

        # move along this normalized vector towards the player at current speed
        self.rect.x += self.dx * self.speedx
        self.rect.y += self.dy * self.speedy

    def check_direction(self):
        if abs(self.dx) > abs(self.dy):
            if self.dx >= 0:
                self.frames = self.walking_frames_l
                self.direction = "right"
            elif self.dx < 0:
                self.frames = self.walking_frames_r
                self.direction = "left"
        else:
            if self.dy >= 0:
                self.frames = self.walking_frames_u
                self.direction = "down"
            elif self.dy < 0:
                self.frames = self.walking_frames_d
                self.direction = "up"

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.centery + 25)
            all_sprites.add(bullet)
            enemy_bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = 0
        self.speedy = 0

        if enemy.direction == "left":
            self.speedx = 5

        if enemy.direction == "right":
            self.speedx = -5

        if enemy.direction == "up":
            self.speedy = 5

        if enemy.direction == "down":
            self.speedy = -5

    def update(self):
        self.scrolling()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0 or self.rect.top> HEIGHT:
            self.kill()
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.kill()

    def scrolling(self):
        self.rect.x += -player.speedx
        self.rect.y += -player.speedy


enemy = Enemy(100, -200)
enemy2 = Enemy(680, -200)
enemy3 = Enemy(-900, 500)
enemy4 = Enemy(-100, 100)
all_sprites.add(enemy)
all_sprites.add(enemy2)
all_sprites.add(enemy3)
all_sprites.add(enemy4)
enemy_sprites.add(enemy)
enemy_sprites.add(enemy2)
enemy_sprites.add(enemy3)
enemy_sprites.add(enemy4)
