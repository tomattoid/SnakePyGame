import runpy
import pygame
import requests
from pygame.locals import KEYDOWN
from config import WIDTH, HEIGHT, FPS, BLACK, GAME_SPEED, SERVER_URL
from snake import Snake
from apple import Apple
from ui import (Win, GameOver, Start, Pause, Menu, Play,
                Leaderboard, Settings, Quit)
from sound import SoundPlayer


class Game():
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.sound_player = SoundPlayer()
        self.player = Snake()
        self.apple = Apple()
        self.pause = Pause()
        self.game_over = GameOver()
        self.you_win = Win()
        self.start = Start()
        self.menu = Menu()
        self.play = Play()
        self.leaderboard = Leaderboard()
        self.settings = Settings()
        self.quit = Quit()

        self.game_sprites = pygame.sprite.Group()
        self.start_sprites = pygame.sprite.Group()
        self.lose_sprites = pygame.sprite.Group()
        self.win_sprite = pygame.sprite.Group()
        self.pause_sprite = pygame.sprite.Group()
        self.main_menu_sprites = pygame.sprite.Group()

        self.game_sprites.add([self.player.parts[0], self.player.parts[1],
                               self.apple])
        self.lose_sprites.add(self.game_over)
        self.win_sprite.add(self.you_win)
        self.pause_sprite.add(self.pause)
        self.start_sprites.add(self.start)
        self.main_menu_list = [self.menu, self.play,
                               self.leaderboard, self.settings,
                               self.quit]
        self.main_menu_sprites.add(self.main_menu_list)

        self.MUSIC_END = pygame.USEREVENT + 1
        self.SNAKE_MOVE = pygame.USEREVENT + 2
        self.MENU_ITEM_BLINK = pygame.USEREVENT + 3

        self.sound_player.set_end_event(self.MUSIC_END)
        self.main_menu()

    def init_game(self):
        self.game_sprites.remove(self.player.parts)
        self.game_sprites.remove(self.apple)
        self.player = Snake()
        self.apple = Apple()
        self.game_sprites.add([self.player.parts[0],
                              self.player.parts[1],
                              self.apple])

    def main_menu(self):
        loop = True
        selected = 0
        pygame.time.set_timer(self.MENU_ITEM_BLINK, GAME_SPEED*5)
        while loop:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.main_menu_list[selected + 1].image.set_alpha(255)
                        selected = (selected + 1) % 4
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.main_menu_list[selected + 1].image.set_alpha(255)
                        selected = (selected - 1) % 4
                    if event.key == pygame.K_RETURN:
                        if selected == 0:
                            loop = False
                        if selected == 3:
                            pygame.quit()
                if event.type == self.MENU_ITEM_BLINK:
                    self.main_menu_list[selected + 1].update()
                    pygame.time.set_timer(self.MENU_ITEM_BLINK, GAME_SPEED*5)
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.screen.fill(BLACK)
            self.main_menu_sprites.draw(self.screen)
            pygame.display.flip()
        self.play_game()

    def check_movement(self, event: pygame.event.Event):
        if ((event.key == pygame.K_a or event.key == pygame.K_LEFT) and not
           (self.player.get_xy(0)[0] - 20 == self.player.get_xy(1)[0] and
           self.player.get_xy(0)[1] == self.player.get_xy(1)[1])):
            self.player.parts[0].speed_x = -20
            self.player.parts[0].speed_y = 0
        if ((event.key == pygame.K_d or event.key == pygame.K_RIGHT) and not
            (self.player.get_xy(0)[0] + 20 == self.player.get_xy(1)[0] and
           self.player.get_xy(0)[1] == self.player.get_xy(1)[1])):
            self.player.parts[0].speed_x = 20
            self.player.parts[0].speed_y = 0
        if ((event.key == pygame.K_w or event.key == pygame.K_UP) and not
           (self.player.get_xy(0)[1] - 20 == self.player.get_xy(1)[1] and
           self.player.get_xy(0)[0] == self.player.get_xy(1)[0])):
            self.player.parts[0].speed_y = -20
            self.player.parts[0].speed_x = 0
        if ((event.key == pygame.K_s or event.key == pygame.K_DOWN) and not
           (self.player.get_xy(0)[1] + 20 == self.player.get_xy(1)[1] and
           self.player.get_xy(0)[0] == self.player.get_xy(1)[0])):
            self.player.parts[0].speed_y = 20
            self.player.parts[0].speed_x = 0

    def collect_apple(self, coordinates):
        self.player.add_element()
        self.game_sprites.remove(self.apple)
        self.game_sprites.add(self.player.parts[-1])
        if len(self.player.parts) == (WIDTH/20) ** 2:
            self.win()
            self.sound_player.play_victory_snd()
        else:
            self.apple = Apple()
            while self.apple.rect.center in coordinates:
                self.apple = Apple()
            self.game_sprites.add(self.apple)
            self.sound_player.play_collect_snd()

    def lose(self):
        self.sound_player.play_lose_snd()
        self.sound_player.stop_music()

        data = {
            'name': 'Antik',
            'score': len(self.player.parts)
        }

        response = requests.post(SERVER_URL + '/player', json=data)
        print(response.text)

        loop = True
        while loop:
            ev = pygame.event.get()
            self.clock.tick(FPS)
            for event in ev:
                if event.type == pygame.QUIT:
                    pygame.quit()
                if (event.type == KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                if (event.type == KEYDOWN and event.key == pygame.K_r):
                    runpy.run_path(path_name='main.py')
                    loop = False
            self.screen.fill(BLACK)
            self.lose_sprites.draw(self.screen)
            pygame.display.flip()

    def pause_game(self):
        loop = True
        ev = pygame.event.get()
        self.sound_player.set_music_volume(0.1)
        while loop:
            ev = pygame.event.get()
            self.clock.tick(FPS)
            for event in ev:
                if event.type == self.MUSIC_END:
                    self.sound_player.play_music()
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                    if event.key == pygame.K_r:
                        self.init_game()
                        loop = False
                        self.play_game()
                    if event.key == pygame.K_m:
                        self.init_game()
                        loop = False
                        self.main_menu()
                    if event.key == pygame.K_ESCAPE:
                        loop = False
                        self.play_game()
                self.screen.fill(BLACK)
                self.pause_sprite.draw(self.screen)
                pygame.display.flip()

    def win(self):
        self.sound_player.play_victory_snd()
        self.sound_player.stop_music()
        loop = True

        while loop:
            ev = pygame.event.get()
            self.clock.tick(FPS)
            for event in ev:
                if event.type == pygame.QUIT:
                    loop = False
                if event.type == pygame.MOUSEBUTTONUP:
                    loop = False
            self.screen.fill(BLACK)
            self.win_sprite.draw(self.screen)
            pygame.display.flip()

    def play_game(self):
        loop = True
        coords = []
        self.sound_player.set_music_volume(0.4)
        pygame.time.set_timer(self.SNAKE_MOVE, GAME_SPEED)
        while loop:
            self.clock.tick(FPS)
            ev = pygame.event.get()
            if loop:
                for event in ev:
                    if (event.type == self.MUSIC_END or
                       not pygame.mixer.music.get_busy()):
                        self.sound_player.play_music()

                    if event.type == pygame.QUIT:
                        loop = False
                        pygame.quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            loop = False
                            self.pause_game()
                        self.check_movement(event)

                    if event.type == self.SNAKE_MOVE:
                        pygame.time.set_timer(self.SNAKE_MOVE, GAME_SPEED)
                        self.game_sprites.update()
                        coords.clear()
                        for idx in range(1, len(self.player.parts)):
                            coords.append(self.player.parts[idx].rect.center)
                        self.player.update_speed()

                        if (self.player.get_xy(0)[0] ==
                           self.apple.rect.centerx and
                           self.player.get_xy(0)[1] ==
                           self.apple.rect.centery):
                            self.collect_apple(coords)

                        if (self.player.get_xy(0) in coords or
                           self.player.get_xy(0)[0] <= 0 or
                           self.player.get_xy(0)[1] <= 0 or
                           self.player.get_xy(0)[0] >= WIDTH or
                           self.player.get_xy(0)[1] >= HEIGHT):
                            loop = False
                            self.lose()

                self.screen.fill(BLACK)
                self.game_sprites.draw(self.screen)

            pygame.display.flip()
