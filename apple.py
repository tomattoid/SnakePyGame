import pygame
import random
from config import WIDTH, HEIGHT, RED


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH/20 - 5, HEIGHT/20 - 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, (WIDTH-20)/20) * 20 + 10,
                            random.randint(0, (WIDTH-20)/20) * 20 + 10)
