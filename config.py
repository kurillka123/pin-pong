from pathlib import Path
RED = (255, 0, 0)               # красный
GREEN = (0, 255, 0)             # зелёный
BLUE = (0, 0, 255)              # синий
BLACK = (0, 0, 0)               # чёрный
WHITE = (255, 255, 255)         # белый
FPS = 80                       # кол-во отрисованных кадров в секунду
ANGLE = 65

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / 'assets'
SOUNDS_DIR = ASSETS_DIR / 'sounds'
FONTS_DIR = ASSETS_DIR / 'fonts'