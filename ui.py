import pygame
from config import (WIDTH, HEIGHT, start_img, game_over_img, pause_img,
                    restart_img, WHITE, you_win_img, play_img,
                    quit_menu_img, leaderboard_img, settings_img, menu_img)


class Start(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(start_img)
        self.image = pygame.transform.scale(self.image,
                                            (WIDTH / 1.5, HEIGHT / 2))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)


class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(game_over_img)
        self.image = pygame.transform.scale(self.image,
                                            (WIDTH / 1.5, HEIGHT / 2))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/3)


class Pause(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pause_img)
        self.image = pygame.transform.scale(self.image,
                                            (WIDTH / 1.2, HEIGHT / 1.4))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)


class Restart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(restart_img).convert()
        self.image = pygame.transform.scale(self.image,
                                            (WIDTH / 3, HEIGHT / 6))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 3, HEIGHT/1.5)


class Win(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(you_win_img)
        self.image = pygame.transform.scale(self.image,
                                            (WIDTH / 1.5, HEIGHT / 2))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)


class Menu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(menu_img)
        self.image = pygame.transform.scale(self.image,
                                            (WIDTH / 1.5, HEIGHT / 1.5))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2.4)


class Play(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(play_img)
        self.image = pygame.transform.scale(self.image,
                                            (WIDTH / 1.5, HEIGHT / 1.5))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2.2)

    def update(self):
        if self.image.get_alpha() == 255:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)


class Leaderboard_ui(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(leaderboard_img)
        self.image = pygame.transform.scale(self.image,
                                            (WIDTH / 1.5, HEIGHT / 1.5))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

    def update(self):
        if self.image.get_alpha() == 255:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)


class Settings_ui(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(settings_img)
        self.image = pygame.transform.scale(self.image,
                                            (WIDTH / 1.5, HEIGHT / 1.5))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/1.8)

    def update(self):
        if self.image.get_alpha() == 255:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)


class Quit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(quit_menu_img)
        self.image = pygame.transform.scale(self.image,
                                            (WIDTH / 1.5, HEIGHT / 1.5))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT / 1.65)

    def update(self):
        if self.image.get_alpha() == 255:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)
