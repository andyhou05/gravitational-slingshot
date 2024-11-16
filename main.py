import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Store the circles as (position, size)
circles = []

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
                # Get mouse position
                mouse_pos = pygame.mouse.get_pos()
                # Random size for the circle
                size = random.randint(10, 20)
                # Add circle data to the list
                circles.append((mouse_pos, size))
                print(circles)

    # Fill the screen with a color to wipe away anything from the last frame
    screen.fill("black")

    # Draw all circles stored in the list
    for pos, size in circles:
        pygame.draw.circle(screen, BLUE, pos, size)

    # Flip the display to put your work on the screen
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()
