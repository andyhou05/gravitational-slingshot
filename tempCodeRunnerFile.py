start_position = positions[0]
    pygame.draw.ellipse(screen, "Green", (start_position.position[0], start_position.position[1], 200, 150))
    my_image = pygame.image.load("pictures/grass.png")
    my_image = pygame.transform.scale(my_image, (200, 150))
    circular_image = pygame.Surface(start_position.position, pygame.SRCALPHA)
    image_rect = my_image.get_rect(topleft=start_position.position)
    screen.blit(my_image, image_rect)