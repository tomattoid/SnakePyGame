import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
game_over_img = os.path.join(img_folder, 'gameover.png')
restart_img = os.path.join(img_folder, 'restart.png')
quit_img = os.path.join(img_folder, 'quit.png')

WIDTH = 480
HEIGHT = WIDTH
FPS = 60
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)