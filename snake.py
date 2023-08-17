from typing import Any
import pygame
from config import *

class SnakeElement(pygame.sprite.Sprite):
    def __init__(self, coordinates, speed_x=0, speed_y=0, color=WHITE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH/20 - 5, WIDTH/20 - 5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (coordinates[0], coordinates[1])
        self.speed_x = speed_x
        self.speed_y = speed_y
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class Snake:
    def __init__(self):
        self.elements = []
        self.elements.append(SnakeElement((30, 10), speed_x=20, color=GREY))
        self.add_element()
    
    def get_direction(self, idx):
        return (self.elements[idx].speed_x, self.elements[idx].speed_y)
    
    def get_coordinates(self, idx):
        return self.elements[idx].rect.center
    
    def add_element(self):
        coordinates = (self.get_coordinates(-1)[0] - self.get_direction(-1)[0], self.get_coordinates(-1)[1] - self.get_direction(-1)[1])
        self.elements.append(SnakeElement(coordinates, self.get_direction(-1)[0], self.get_direction(-1)[1]))
    
    def update_speed(self):
        if len(self.elements) > 1:
            for element_idx in range(len(self.elements) - 1, 0, -1):
                self.elements[element_idx].speed_x = self.elements[element_idx - 1].speed_x
                self.elements[element_idx].speed_y = self.elements[element_idx - 1].speed_y