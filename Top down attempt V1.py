# Plans for a Top Down Shooter
# Make a character from a bird's eye view
# Make him shoot
    # Only 4 directions for now


import pygame
import time
from constant import *
from player import *
from spritesheet_functions import SpriteSheet

# Initialises pygame and creates a window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()


player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


# Game loop
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)
    # Process input(events)
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()

    # Render / draw
    screen.fill(WHITE)
    all_sprites.draw(screen)
    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
