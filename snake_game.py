import pygame
import random

pygame.init()

width = 600
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

snake_x = 100
snake_y = 100

snake_size = 20
speed = 10

food_x = random.randrange(0, width, 20)
food_y = random.randrange(0, height, 20)

clock = pygame.time.Clock()

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= speed
    if keys[pygame.K_RIGHT]:
        snake_x += speed
    if keys[pygame.K_UP]:
        snake_y -= speed
    if keys[pygame.K_DOWN]:
        snake_y += speed
    pygame.draw.rect(screen, (0, 255, 0),
                     [snake_x, snake_y, snake_size, snake_size])

    pygame.draw.rect(screen, (255, 0, 0),
                     [food_x, food_y, snake_size, snake_size])

    pygame.display.update()
    clock.tick(15)

pygame.quit()