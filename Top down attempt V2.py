# Plans for a Top Down Shooter
# Make a character from a bird's eye view
# Add sidescrolling to the thing


import pygame
import time
from player import *
from enemy import *
from backround import *
from constant import *
from spritesheet_functions import SpriteSheet
import sys

# Initialises pygame and creates a window
pygame.init()
pygame.mixer.init()


pygame.display.set_caption("Top Down Shooter")
clock = pygame.time.Clock()


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
    #backround_list.update()
    tile_group.update()

    # Render / draw
    screen.fill(BLACK)
    #backround_list.draw(screen)
    tile_group.draw(screen)
    all_sprites.draw(screen)


    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
