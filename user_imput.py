import pygame
from config import WHITE, BLACK, WIDTH, HEIGHT, RED


def enter_user_name(self):
    loop = True
    user_name = ''
    self.screen.fill(BLACK)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                elif event.key == pygame.K_RETURN:
                    loop = False
                elif event.unicode.isalnum() and len(user_name) < 13:
                    user_name += event.unicode

        self.screen.fill(BLACK)

        text = self.font.render('ENTER YOUR NAME', True, RED)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH/2, HEIGHT/4)
        self.screen.blit(text, text_rect)

        user_text = self.font.render(user_name, True, WHITE)
        user_text_rect = user_text.get_rect()
        user_text_rect.center = (WIDTH/2, HEIGHT/2)
        self.screen.blit(user_text, user_text_rect)

        pygame.display.flip()

    return user_name
