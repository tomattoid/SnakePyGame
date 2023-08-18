import runpy
import pygame
import random
from config import *
from snake import Snake
from apple import Apple
from ui import *


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
ui_sprites = pygame.sprite.Group()
player = Snake()
apple = Apple()
all_sprites.add(player.elements[0])
all_sprites.add(player.elements[1])
all_sprites.add(apple)

quit_sprite = Quit()
game_over_sprite = GameOver()
restart_sprite = Restart()
ui_sprites.add([quit_sprite, restart_sprite, game_over_sprite])

snake_move_event = pygame.USEREVENT + 1
pygame.time.set_timer(snake_move_event, 200)
running = True
eat = False
game_over = False
coordinates = []
while running:
    clock.tick(FPS)
    ev = pygame.event.get()
    if not game_over:       
        
        coordinates.clear()
        for element in player.elements:
            coordinates.append(element.rect.center)
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player.get_direction(0)[0] <= 0:
                    player.elements[0].speed_x = -20
                    player.elements[0].speed_y = 0
                if event.key == pygame.K_RIGHT and player.get_direction(0)[0] >= 0:
                    player.elements[0].speed_x = 20
                    player.elements[0].speed_y = 0
                if event.key == pygame.K_UP and player.get_direction(0)[1] <= 0:
                    player.elements[0].speed_y = -20
                    player.elements[0].speed_x = 0
                if event.key == pygame.K_DOWN and player.get_direction(0)[1] >= 0:
                    player.elements[0].speed_y = 20
                    player.elements[0].speed_x = 0
            if event.type == snake_move_event:
                pygame.time.set_timer(snake_move_event, 150)
                all_sprites.update()
                player.update_speed()
                if (player.get_coordinates(0)[0] == apple.rect.centerx and 
                    player.get_coordinates(0)[1] == apple.rect.centery):
                    player.add_element()
                    all_sprites.remove(apple)
                    all_sprites.add(player.elements[-1])
                    apple = Apple()
                    while apple.rect.center in coordinates:
                        apple = Apple()
                    all_sprites.add(apple)
                    eat = False 
                if (player.get_coordinates(0) in coordinates or player.get_coordinates(0)[0] <= 0 or player.get_coordinates(0)[1] <= 0 or
                    player.get_coordinates(0)[0] >= WIDTH or player.get_coordinates(0)[1] >= HEIGHT):
                    game_over = True
 
        screen.fill(BLACK)
        all_sprites.draw(screen)
    else:
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in ui_sprites if s.rect.collidepoint(pos)]
            if pygame.mouse.get_pressed()[0] and quit_sprite.rect.collidepoint(pygame.mouse.get_pos()):
                running = False
            if pygame.mouse.get_pressed()[0] and restart_sprite.rect.collidepoint(pygame.mouse.get_pos()):
                runpy.run_path(path_name='main.py')
                running = False
        screen.fill(BLACK)
        ui_sprites.draw(screen)
    pygame.display.flip()
    
pygame.quit()