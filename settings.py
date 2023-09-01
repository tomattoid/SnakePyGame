import pygame
from config import GAME_SPEED, WHITE, HEIGHT, WIDTH, RED, BLACK, FPS
from enum_ceate import SettnigMenuItem, FontSize


class Settings():
    def __init__(self, screen, sound) -> None:
        self.screen = screen
        self.sound_player = sound
        self.clock = pygame.time.Clock()
        self.MENU_ITEM_BLINK = pygame.USEREVENT + 3

    def SettingMenu(self):
        loop = True
        pygame.time.set_timer(self.MENU_ITEM_BLINK, GAME_SPEED)
        setting_text = pygame.font.Font('./fonts/retro.ttf', FontSize.LARGE)
        setting_text_m = pygame.font.Font('./fonts/retro.ttf', FontSize.MEDIUM)
        # setting_text_s = pygame.font.Font('./fonts/retro.ttf',
        #  FontSize.SMALL)

        setting_title = setting_text.render('SETTINGS', True, (RED))
        place = setting_title.get_rect(center=(HEIGHT/2, WIDTH/8))

        sound = setting_text_m.render('SOUND', True, (WHITE))
        music_volume = setting_text_m.render('VLOUME', True, (WHITE))
        back = setting_text_m.render('BACK', True, (WHITE))

        setting_menu_list = [sound, music_volume, back]
        selected = 0

        sound_enabled = True

        while loop:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if not sound_enabled:
                    self.sound_player.set_music_volume(0)
                else:
                    self.sound_player.set_music_volume(0.4)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        setting_menu_list[selected].set_alpha(255)
                        selected = (selected + 1) % len(setting_menu_list)
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        setting_menu_list[selected].set_alpha(255)
                        selected = (selected - 1) % len(setting_menu_list)
                    if event.key == pygame.K_RETURN:
                        loop = True
                        if selected == SettnigMenuItem.SOUND:
                            sound_enabled = not sound_enabled
                        if selected == SettnigMenuItem.MUSIC_VOLUME:
                            pass  # Действия при выборе пункта MUSIC_VOLUME
                        if selected == SettnigMenuItem.BACK:
                            return
                if event.type == self.MENU_ITEM_BLINK:
                    setting_menu_list[selected].set_alpha(
                        255 - setting_menu_list[selected].get_alpha())
                    pygame.time.set_timer(self.MENU_ITEM_BLINK, GAME_SPEED)

                self.screen.fill(BLACK)
                margin_top = 100
                for i, item in enumerate(setting_menu_list):
                    self.screen.blit(setting_title, place)
                    place_item = item.get_rect(center=(WIDTH/2,
                                                       margin_top))
                    self.screen.blit(item, place_item)
                    margin_top += 30

                sound_status = setting_text_m.render('ON' if sound_enabled
                                                     else 'OFF', True,
                                                     (WHITE))
                place_status = sound_status.get_rect(center=(WIDTH/2 + 100,
                                                             100))
                self.screen.blit(sound_status, place_status)
                pygame.display.flip()
        pass
