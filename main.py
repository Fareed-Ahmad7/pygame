import pygame

# initialize the pygame

pygame.init()
# creating screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Physics Simulator")
icon = pygame.image.load('gravity-3.png')
pygame.display.set_icon(icon)

# backqround image
background = pygame.image.load('ϴ.png')

# game loop
running = True
while running:

    # rgb- red ,green ,blue
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


#  updating screen
    pygame.display.update()
