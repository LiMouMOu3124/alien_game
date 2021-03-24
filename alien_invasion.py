

import pygame
from ship import Ship
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #设置背景色
    bg_color = (230,230,230)

    #创建飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()


    #开始游戏主循环
    while True:

        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)
        gf.update_bullets(bullets)

        print(len(bullets))

run_game()