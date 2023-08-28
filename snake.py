import json
import pygame
from config import WIDTH, HEIGHT, WHITE, GREY


class SnakeElement(pygame.sprite.Sprite):
    def __init__(self, coordinates, speed_x=0, speed_y=0, color=WHITE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH/20 - 5, HEIGHT/20 - 5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (coordinates[0], coordinates[1])
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def to_dict(self):
        return {
            "coordinates": (self.rect.centerx, self.rect.centery),
            "speed_x": self.speed_x,
            "speed_y": self.speed_y
        }

class Snake:
    def __init__(self):
        self.parts = []
        self.parts.append(SnakeElement((30, 10), speed_x=20, color=GREY))
        self.add_element()

    def get_direction(self, idx):
        return (self.parts[idx].speed_x, self.parts[idx].speed_y)

    def get_xy(self, idx):
        return self.parts[idx].rect.center

    def add_element(self):
        coordinates = (self.get_xy(-1)[0] - self.get_direction(-1)[0],
                       self.get_xy(-1)[1] - self.get_direction(-1)[1])
        self.parts.append(SnakeElement(coordinates,
                                       self.get_direction(-1)[0],
                                       self.get_direction(-1)[1]))

    def update_speed(self):
        if len(self.parts) > 1:
            for idx in range(len(self.parts) - 1, 0, -1):
                self.parts[idx].speed_x = self.parts[idx - 1].speed_x
                self.parts[idx].speed_y = self.parts[idx - 1].speed_y

    def get_next_pos(self):
        return (self.parts[0].rect.centerx + self.get_direction(0)[0],
                self.parts[0].rect.centery + self.get_direction(0)[1])

    def to_dict(self):
        return {
            "parts": [part.to_dict() for part in self.parts]
        }