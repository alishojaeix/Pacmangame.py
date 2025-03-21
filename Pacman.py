import pygame
import sys

Initialize pygame
pygame.init()

Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

Pac-Man properties
pacman_x, pacman_y = 50, 50
pacman_speed = 5

Ghost properties
ghost_x, ghost_y = 400, 300
ghost_speed = 3

Load images from online sources
PACMAN_IMG_URL = "https://i.imgur.com/4JZJZJZ.png"  # Replace with a valid URL
GHOST_IMG_URL = "https://i.imgur.com/9Z9Z9Z9.png"    # Replace with a valid URL

Load images
pacman_img = pygame.image.load(pygame.image.load(PACMAN_IMG_URL))
ghost_img = pygame.image.load(pygame.image.load(GHOST_IMG_URL))

Main game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     Move Pac-Man
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    Move Ghost
    if ghost_x < pacman_x:
        ghost_x += ghost_speed
    elif ghost_x > pacman_x:
        ghost_x -= ghost_speed
    if ghost_y < pacman_y:
        ghost_y += ghost_speed
    elif ghost_y > pacman_y:
        ghost_y -= ghost_speed

     Draw Pac-Man and Ghost
    screen.blit(pacman_img, (pacman_x, pacman_y))
    screen.blit(ghost_img, (ghost_x, ghost_y))

    Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
