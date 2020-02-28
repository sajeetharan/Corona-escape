TITLE = "Corona Escape"
WIDTH = 800
HEIGHT = 600
FPS = 40
FONT_NAME = "arial"
HIGHSCORE_FILE = "highscore.txt"
SPRITESHEET = "spritesheet.png"
GRASS_TILE = "grass_tile.png"
STONE_TILE = "stone_tile.png"
JUMP_SOUND = "jump.wav"
THEME_MUSIC = "theme.ogg"
MENU_MUSIC = "menu.wav"
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POWERUP_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0
PLAYER_ACCELERATION = 0.50
PLAYER_FRICTION = -0.1
PLAYER_GRAVITY = 0.5
PLAYER_JUMP_SPEED = 18
BACKGROUND_COLOR = (0, 168, 255)
GREY = BACKGROUND_COLOR #(128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
TURQUOISE = (0, 255, 255)
PINK = (255, 0, 255)
PLATFORM_LIST = [ (0, HEIGHT-40), # base ground
                  (WIDTH/2-50, HEIGHT*3/4), # 450
                  (200, HEIGHT*2/4+50), # 350
                  (350, HEIGHT*2/4-50), # 250
                  (200, HEIGHT*1/4, 100), # 150
                  (350, HEIGHT*1/4-100), # 50
                  (200, HEIGHT*1/4-200)] # -50
CAPSULE_POWER = 40
