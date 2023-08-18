import runpy
import pygame
from config import WIDTH, HEIGHT, FPS, BLACK
from snake import Snake
from apple import Apple
from ui import Quit, Restart, Win, GameOver


def check_movement(player: Snake, event: pygame.event.Event):
    if (event.key == pygame.K_LEFT and not
        (player.get_coordinates(0)[0] - 20 == player.get_coordinates(1)[0] and
         player.get_coordinates(0)[1] == player.get_coordinates(1)[1])):
        player.parts[0].speed_x = -20
        player.parts[0].speed_y = 0
    if (event.key == pygame.K_RIGHT and not
        (player.get_coordinates(0)[0] + 20 == player.get_coordinates(1)[0] and
         player.get_coordinates(0)[1] == player.get_coordinates(1)[1])):
        player.parts[0].speed_x = 20
        player.parts[0].speed_y = 0
    if (event.key == pygame.K_UP and not
        (player.get_coordinates(0)[1] - 20 == player.get_coordinates(1)[1] and
         player.get_coordinates(0)[0] == player.get_coordinates(1)[0])):
        player.parts[0].speed_y = -20
        player.parts[0].speed_x = 0
    if (event.key == pygame.K_DOWN and not
        (player.get_coordinates(0)[1] + 20 == player.get_coordinates(1)[1] and
         player.get_coordinates(0)[0] == player.get_coordinates(1)[0])):
        player.parts[0].speed_y = 20
        player.parts[0].speed_x = 0


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
lose_sprites = pygame.sprite.Group()
win_sprite = pygame.sprite.Group()
player = Snake()
apple = Apple()
you_win_sprite = Win()
all_sprites.add(player.parts[0])
all_sprites.add(player.parts[1])
all_sprites.add(apple)

quit_sprite = Quit()
game_over_sprite = GameOver()
restart_sprite = Restart()
lose_sprites.add([quit_sprite, restart_sprite, game_over_sprite])
win_sprite.add(you_win_sprite)

snake_move_event = pygame.USEREVENT + 1
pygame.time.set_timer(snake_move_event, 150)
running = True
eat = False
game_over = False
you_win = False
coordinates = []
while running:

    clock.tick(FPS)
    ev = pygame.event.get()
    if not game_over and not you_win:
        coordinates.clear()
        for element in player.parts:
            coordinates.append(element.rect.center)
        for event in ev:

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                check_movement(player, event)

            if event.type == snake_move_event:
                pygame.time.set_timer(snake_move_event, 150)
                all_sprites.update()
                player.update_speed()
                if (player.get_coordinates(0)[0] == apple.rect.centerx and
                   player.get_coordinates(0)[1] == apple.rect.centery):
                    player.add_element()
                    all_sprites.remove(apple)
                    all_sprites.add(player.parts[-1])
                    if len(player.parts) == (WIDTH/20) ** 2:
                        you_win = True
                    else:
                        apple = Apple()
                        while apple.rect.center in coordinates:
                            apple = Apple()
                        all_sprites.add(apple)
                        eat = False
                if (player.get_coordinates(0)[0] in coordinates or
                   player.get_coordinates(0)[0] <= 0 or
                   player.get_coordinates(0)[1] <= 0 or
                   player.get_coordinates(0)[0] >= WIDTH or
                   player.get_coordinates(0)[1] >= HEIGHT):
                    game_over = True

        screen.fill(BLACK)
        all_sprites.draw(screen)

    elif game_over:
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in lose_sprites if
                                   s.rect.collidepoint(pos)]
            if (pygame.mouse.get_pressed()[0] and
               quit_sprite.rect.collidepoint(pygame.mouse.get_pos())):
                running = False
            if (pygame.mouse.get_pressed()[0] and
               restart_sprite.rect.collidepoint(pygame.mouse.get_pos())):
                runpy.run_path(path_name='main.py')
                running = False
        screen.fill(BLACK)
        lose_sprites.draw(screen)

    elif you_win:
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                running = False
        screen.fill(BLACK)
        win_sprite.draw(screen)
    pygame.display.flip()

pygame.quit()
