import pygame
import random
from models.projectile import Projectile

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Store the projectile objects
projectiles = []

# Colors:
RED = (255, 0, 0)  # For planets
BLUE = (0, 0, 255) # For user body

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Create new projectile
                projectile = Projectile(0, position = pygame.mouse.get_pos(), radius = random.randint(10, 20))
                projectiles.append(projectile)

    # Fill the screen with a color to wipe away anything from the last frame
    screen.fill("black")

    # Draw all circles stored in the list
    for projectile in projectiles:
        pygame.draw.circle(screen, BLUE, projectile.position, projectile.radius)

    # Flip the display to put your work on the screen
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()
