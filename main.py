# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
from config import *
from snake import Snake
from apple import Apple


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Snake()
apple = Apple()
print(apple.rect.center)
all_sprites.add(player.elements[0])
all_sprites.add(player.elements[1])
all_sprites.add(apple)

running = True
eat = False
coordinates = []
while running:
    clock.tick(FPS)
    coordinates.clear()
    for element in player.elements:
        coordinates.append(element.rect.center)
    player.update_speed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player.elements[1].rect.centerx != player.elements[0].rect.centerx - 20:
                player.elements[0].speed_x = -20
                player.elements[0].speed_y = 0
            if event.key == pygame.K_RIGHT and player.elements[1].rect.centerx != player.elements[0].rect.centerx + 20:
                player.elements[0].speed_x = 20
                player.elements[0].speed_y = 0
            if event.key == pygame.K_UP and player.elements[1].rect.centery != player.elements[0].rect.centery - 20:
                player.elements[0].speed_y = -20
                player.elements[0].speed_x = 0
            if event.key == pygame.K_DOWN and player.elements[1].rect.centery != player.elements[0].rect.centery + 20:
                player.elements[0].speed_y = 20
                player.elements[0].speed_x = 0
    if player.elements[0].rect.centerx + player.get_direction(0)[0] == apple.rect.centerx and player.elements[0].rect.centery + player.get_direction(0)[1] == apple.rect.centery:
        eat = True
    all_sprites.update()
    if eat:
        player.add_element()
        all_sprites.remove(apple)
        all_sprites.add(player.elements[-1])
        apple = Apple()
        while apple.rect.center in coordinates:
            apple = Apple()
        all_sprites.add(apple)
        eat = False
    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    pygame.display.flip()

pygame.quit()