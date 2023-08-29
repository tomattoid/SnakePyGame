import pygame
from server_req import ServerReq
from pygame.locals import KEYDOWN
from config import WIDTH, HEIGHT, BLACK, RED, WHITE
from enum_ceate import FontSize


class Leaderboard():
    def __init__(self, screen):
        self.screen = screen

    def show(self):
        self.server_req = ServerReq()
        self.screen.fill(BLACK)
        f1 = pygame.font.Font('./fonts/retro.ttf', FontSize.LARGE)
        text1 = f1.render('LEADERBOARD', True, (RED))
        place = text1.get_rect(center=(HEIGHT/2, WIDTH/8))
        self.screen.blit(text1, place)

        try:
            leaders = self.server_req.get_leaderboard()
            title_font = pygame.font.Font('./fonts/retro.ttf', FontSize.MEDIUM)

            margin_top = 100
            for player in leaders:
                text_player = title_font.render(
                    str(player['score']) + ': ' + player['name'], True,
                    (WHITE))
                place = text_player.get_rect(center=(WIDTH/2, margin_top))
                self.screen.blit(text_player, place)
                margin_top += 30
        except ConnectionError:
            print('error')

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    return
