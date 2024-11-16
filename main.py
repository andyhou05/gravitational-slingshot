import pygame
import random
from models.projectile import Projectile
from models.planet import Planet
from helper import * 

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Store the projectile objects
projectiles = []

# Store the planet objects
planets = [Planet((400, 300), 50)]

# Colors:
RED = (255, 0, 0)  # For planets
BLUE = (0, 0, 255) # For user body

# drag effect
last_pos = None
drawing = False
mouse_position = ()

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Create a new projectile with every mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                projectile = Projectile(position = pygame.mouse.get_pos(), radius = random.randint(10, 20))
                projectiles.append(projectile)
                
                # Keep track of the starting position for drag
                drawing = True
                last_pos = pygame.mouse.get_pos()
                
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                mouse_position = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP:
            # Calculate velocity based on length of drag, we use -1 index since the newest projectile will always be at the end of the projectiles list
            projectiles[-1].velocity = calculate_velocity(last_pos, pygame.mouse.get_pos())
            drawing = False

    # Fill the screen with a color to wipe away anything from the last frame
    screen.fill("black")
    if drawing:
        if last_pos != pygame.mouse.get_pos():
            drag_effect = pygame.draw.line(screen, "white", last_pos, mouse_position, 3)

    
    # Draw the planets
    for planet in planets:
        pygame.draw.circle(screen, RED, planet.position, planet.radius)

    # Draw all circles stored in the list
    for projectile in projectiles:
        pygame.draw.circle(screen, BLUE, projectile.position, projectile.radius)

    # Flip the display to put your work on the screen
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()
