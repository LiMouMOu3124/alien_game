import sys

import pygame


from bullet import Bullet

def check_events(ship,ai_settings,screen,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship,bullets):
    """更新屏幕上的新图像，并切换到新屏幕"""

    # 每次循环都重绘屏幕,用背景色填充屏幕
    for bullets in bullets.sprites():
        bullets.draw_bullet()
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见，是刷新屏幕的作用，从而达到流畅滑动的作用
    pygame.display.flip()

def check_keydown_events(event,ship,ai_settings,screen,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def update_bullets(bullets):
    """更新子弹位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有达到限制，就再发射一颗子弹"""
    #创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullets = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullets)