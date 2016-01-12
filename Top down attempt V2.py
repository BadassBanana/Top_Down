# Plans for a Top Down Shooter
# Make a character from a bird's eye view
# Add sidescrolling to the thing
    # Yeah I don't know how this is going to work...


import pygame
import time
from player import *
from enemy import *
from spritesheet_functions import SpriteSheet
import sys

# Initialises pygame and creates a window
pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pong")
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

    # Render / draw
    screen.fill(WHITE)
    all_sprites.draw(screen)
    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
