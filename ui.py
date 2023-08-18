import pygame
from config import *

class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(game_over_img)
        self.image = pygame.transform.scale(self.image, (WIDTH / 1.5, HEIGHT / 2))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/3)

class Quit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(quit_img).convert()
        self.image = pygame.transform.scale(self.image, (WIDTH / 3, HEIGHT / 6))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/3 * 2, HEIGHT/1.5)

class Restart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(restart_img).convert()
        self.image = pygame.transform.scale(self.image, (WIDTH / 3, HEIGHT / 6))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 3, HEIGHT/1.5)