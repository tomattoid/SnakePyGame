import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
game_over_img = os.path.join(img_folder, 'gameover.png')
restart_img = os.path.join(img_folder, 'restart.png')
quit_img = os.path.join(img_folder, 'quit.png')
you_win_img = os.path.join(img_folder, 'you_win.png')
start_img = os.path.join(img_folder, 'start.png')

WIDTH = 480
HEIGHT = WIDTH
FPS = 60
WHITE = (235, 219, 178)
GREY = (146, 131, 116)
BLACK = (28, 28, 28)
RED = (251, 74, 68)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
