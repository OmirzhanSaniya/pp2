import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)

BALL_RADIUS = 25
BALL_COLOR = (255, 0, 0)
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        ball_y -= 20
    if keys[pygame.K_DOWN]:
        ball_y += 20
    if keys[pygame.K_LEFT]:
        ball_x -= 20
    if keys[pygame.K_RIGHT]:
        ball_x += 20

    ball_x = max(BALL_RADIUS, min(WIDTH - BALL_RADIUS, ball_x))
    ball_y = max(BALL_RADIUS, min(HEIGHT - BALL_RADIUS, ball_y))

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip()
