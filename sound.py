from config import (music1, music2, music3, music4,
                    music5, lose_snd, collect_snd, victory_snd)
import pygame
import random


class SoundPlayer:
    def __init__(self) -> None:
        self.music = []
        self.music += [music1, music2, music3,
                       music4, music5]
        random.shuffle(self.music)
        self.current_music = 0
        self.lose = pygame.mixer.Sound(lose_snd)
        self.collect = pygame.mixer.Sound(collect_snd)
        self.victory = pygame.mixer.Sound(victory_snd)
        self.set_music_volume(0.4)

    def play_lose_snd(self):
        self.lose.play()

    def play_collect_snd(self):
        self.collect.play()

    def play_victory_snd(self):
        self.victory.play()

    def play_music(self):
        pygame.mixer.music.load(self.music[self.current_music])
        pygame.mixer.music.play(1)
        if self.current_music == len(self.music) - 1:
            random.shuffle(self.music)
            self.current_music = 0
        else:
            self.current_music += 1

    def stop_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

    def set_music_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def set_end_event(self, end_event):
        pygame.mixer.music.set_endevent(end_event)
