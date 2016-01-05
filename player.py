import pygame
import time
from constant import *
from spritesheet_functions import SpriteSheet

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    # Sprite for the Player

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.walking_frames_d = [] # Images for animated walking.

        sprite_sheet = SpriteSheet("spritesheet.png")
        image = sprite_sheet.get_image(19, 0, 54, 96)
        self.walking_frames_d.append(image)

        image = sprite_sheet.get_image(169, 0, 54, 96) # Adds up by 150 everytime
        self.walking_frames_d.append(image)

        image = sprite_sheet.get_image(319, 0, 54, 96)
        self.walking_frames_d.append(image)

        image = sprite_sheet.get_image(469, 0, 54, 96)
        self.walking_frames_d.append(image)

        image = sprite_sheet.get_image(619, 0, 54, 96)
        self.walking_frames_d.append(image)

        image = sprite_sheet.get_image(769, 0, 54, 96)
        self.walking_frames_d.append(image)

        image = sprite_sheet.get_image(919, 0, 54, 96)
        self.walking_frames_d.append(image)

        self.image = self.walking_frames_d[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

        self.last_update = pygame.time.get_ticks()
        self.frame = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -2
        if keystate[pygame.K_DOWN]:
            self.speedy = 2
            self.animate_sprite(self.walking_frames_d)
        if keystate[pygame.K_LEFT]:
            self.speedx = -2
        if keystate[pygame.K_RIGHT]:
            self.speedx = 2
        self.rect.y += self.speedy
        self.rect.x += self.speedx

    def animate_sprite(anim_list):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.frame = (self.frame + 1) % 7
            self.image = anim_list[self.frame]