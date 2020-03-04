import pygame

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800,500))

# Title and Icon
pygame.display.set_caption("Totally an adventure game")
the_icon = pygame.image.load('C:/Users/EysiCrazy/Python/T-201-GSKI-Vor-2020/PPP/green_ball_32x32.png')
pygame.display.set_icon(the_icon)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

