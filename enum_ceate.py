import enum


class MenuItem(enum.IntEnum):
    PLAY = 0
    LEADERBOARD = 1
    SETTINGS = 2
    QUIT = 3


class Margin(enum.IntEnum):
    TOP = 5


class FontSize(enum.IntEnum):
    SMALL = 10
    MEDIUM = 15
    LARGE = 20
