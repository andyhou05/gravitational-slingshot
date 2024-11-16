import pygame
from models.projectile import Projectile
from models.planet import Planet
from models.holes import Hole
from helper import *
from models.start import Start
import sqlite3

key = "Leaderboard.db"

connexion = sqlite3.connect(key)
cursor = connexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS leaderboard(id INTEGER PRIMARY KEY, nom TEXT, time FLOAT)")
connexion.commit()
connexion.close()




# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Putt")
clock = pygame.time.Clock()
running = True

bg = pygame.image.load("pictures/hackaton_background.png")
bg = pygame.transform.scale(bg, (800, 600))

# Explosion gif
explosion = pygame.image.load("pictures/explosion.gif")
explosion = pygame.transform.scale(explosion, (50, 50))

# Store the projectile objects
projectiles = []

# Store the planet objects
planets = [Planet((200,100),50),Planet((400, 300), 50)]

# Store the holes
holes = [Hole((600,500),30),Hole((100,100),30)]

# Store starting positions
positions = [Start((100,400)),Start((500, 400))]

# Colors:
RED = (255, 0, 0)  # For planets
BLUE = (0, 0, 255) # For user body

# drag effect
last_pos = (0,0)
drawing = False
x = 0
y = 0
target_x = 0
target_y = 0
mouse_position = (0,0)

# Level_counter
level = 1





while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Create a new projectile with every mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if event.pos[0] >= positions[0].position[0] and event.pos[0] <= positions[0].position[0]+200 and event.pos[1] >= positions[0].position[1] and event.pos[1] <= positions[0].position[1]+150:
                    projectile = Projectile(position = pygame.mouse.get_pos(), radius = 25)
                    projectiles.append(projectile)
                    drawing = True
                    last_pos = pygame.mouse.get_pos()
                    mouse_position = pygame.mouse.get_pos()
                    target_x, target_y = last_pos
                



        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                mouse_position = pygame.mouse.get_pos()
                x, y = mouse_position
                
        elif event.type == pygame.MOUSEBUTTONUP:


            # Calculate velocity based on length of drag, we use -1 index since the newest projectile will always be at the end of the projectiles list
            if len(projectiles) !=0:
                projectiles[-1].velocity = calculate_velocity(pygame.mouse.get_pos(), last_pos)


            drawing = False



    screen.blit(bg,(0,0))
    
    
    # Draw the planets
    planet = planets[0]
    pygame.draw.circle(screen, "black", planet.position, planet.radius)
    my_image = pygame.image.load("pictures/sun.png")
    my_image = pygame.transform.scale(my_image, (planet.radius*2+10, planet.radius*2+5))
    circular_image = pygame.Surface((50, 50), pygame.SRCALPHA)
    image_rect = my_image.get_rect(center=planet.position)
    screen.blit(my_image, image_rect)

    hole = holes[0]
    pygame.draw.circle(screen, "yellow", hole.position, hole.radius)


    # Draw the starting zone
    start_position = positions[0]
    ellipse_width, ellipse_height = 200, 150

    # Create a transparent surface for the ellipse
    ellipse_surface = pygame.Surface((ellipse_width, ellipse_height), pygame.SRCALPHA)

    # Draw the ellipse on the transparent surface
    pygame.draw.ellipse(ellipse_surface, (255, 255, 255, 255), (0, 0, ellipse_width, ellipse_height))

    # Load and scale the image
    my_image = pygame.image.load("pictures/grass.png")
    my_image = pygame.transform.scale(my_image, (ellipse_width, ellipse_height))

    # Blit the image onto the ellipse surface
    ellipse_surface.blit(my_image, (0,0), special_flags=pygame.BLEND_RGBA_MIN)

    # Draw the elliptical image onto the main screen
    ellipse_rect = ellipse_surface.get_rect(topleft=start_position.position)
    screen.blit(ellipse_surface, ellipse_rect)

    # Draw all circles stored in the list
    for projectile in projectiles:
        pygame.draw.circle(screen, BLUE, projectile.position, projectile.radius)
        if projectile.velocity != 0:
            projectile.position = ((projectile.position[0] + projectile.velocity[0]/50), (projectile.position[1] + projectile.velocity[1]/50))
            projectile.velocity = (projectile.velocity[0] + gravitational_acceleration(projectile.position, planets[0])[0]), (projectile.velocity[1] + gravitational_acceleration(projectile.position, planets[0])[1])
        if distance_calc(projectile.position, planet.position) <= projectile.radius + planet.radius:
            projectiles.remove(projectile)

    if drawing:
        if last_pos != pygame.mouse.get_pos():
            drag_effect = pygame.draw.line(screen, "white", last_pos, mouse_position, 3)
            
    elif not drawing:
        if last_pos != mouse_position:
            # Slingshot animation
            diff_x = target_x - x
            x += diff_x / 3
            diff_y = target_y - y
            y += diff_y / 3
            drag_effect = pygame.draw.line(screen, "white", (x,y), last_pos, 3)
            mouse_position = (round(x),round(y))
    

    # Draw all circles stored in the list
    for projectile in projectiles:

        # IMAGE CONNECTED TO THE CIRCLE
        pygame.draw.circle(screen,"light blue", projectile.position, projectile.radius)
        my_image = pygame.image.load("pictures/earth.png")
        my_image = pygame.transform.scale(my_image, (projectile.radius*2+10, projectile.radius*2+5))
        circular_image = pygame.Surface((1, 1), pygame.SRCALPHA)
        image_rect = my_image.get_rect(center=projectile.position)
        screen.blit(my_image, image_rect)


        if projectile.velocity != 0:
            projectile.position = ((projectile.position[0] + projectile.velocity[0]/50), (projectile.position[1] + projectile.velocity[1]/50))
            projectile.velocity = (projectile.velocity[0] + gravitational_acceleration(projectile.position, planets[0])[0]), (projectile.velocity[1] + gravitational_acceleration(projectile.position, planets[0])[1])
        if distance_calc(projectile.position,planet.position) <= projectile.radius + planet.radius:
            projectiles.remove(projectile)
        if projectile.position[0] >= 850 or projectile.position[0] <= -50 or projectile.position[1] >= 650 or projectile.position[1] <=-50:
            projectiles.remove(projectile)
        if distance_calc(projectile.position,hole.position) <= projectile.radius + hole.radius:

            if len(planets) == 1:
                print("u finished")
            else:
                projectiles.clear()
                planets.pop(0)
                holes.pop(0)
                positions.pop(0)
                level += 1
















    # title of level
    font = pygame.font.SysFont("Arial", 35)
    text = f"Level {level}"
    text_surface = font.render(text, True, "white")
    screen.blit(text_surface,(350,50))

    # Flip the display to put your work on the screen
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()
