import os

game_folder = os.path.dirname(__file__)

img_folder = os.path.join(game_folder, 'img')
game_over_img = os.path.join(img_folder, 'gameover.png')
restart_img = os.path.join(img_folder, 'restart.png')
quit_img = os.path.join(img_folder, 'quit.png')
you_win_img = os.path.join(img_folder, 'you_win.png')
start_img = os.path.join(img_folder, 'start.png')
pause_img = os.path.join(img_folder, 'pause.png')
leaderboard_img = os.path.join(img_folder, 'leaderboard.png')
quit_menu_img = os.path.join(img_folder, 'quit.png')
menu_img = os.path.join(img_folder, 'menu.png')
play_img = os.path.join(img_folder, 'play.png')
settings_img = os.path.join(img_folder, 'settings.png')

snd_folder = os.path.join(game_folder, 'snd')
music1 = os.path.join(snd_folder, 'music1.wav')
music2 = os.path.join(snd_folder, 'music2.wav')
music3 = os.path.join(snd_folder, 'music3.wav')
music4 = os.path.join(snd_folder, 'music4.wav')
music5 = os.path.join(snd_folder, 'music5.wav')
lose_snd = os.path.join(snd_folder, 'game_over_sound.wav')
collect_snd = os.path.join(snd_folder, 'collect.wav')
victory_snd = os.path.join(snd_folder, 'victory.wav')

WIDTH = 480
HEIGHT = WIDTH
FPS = 60
GAME_SPEED = 150
WHITE = (235, 219, 178)
GREY = (146, 131, 116)
BLACK = (28, 28, 28)
RED = (251, 73, 52)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SERVER_URL = 'http://Antik88.pythonanywhere.com'
