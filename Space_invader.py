import math

import random

import pygame

SCREEN_WIDTH=800

SCREEN_HEIGHT=500

PLAYER_STARTX=370

PLAYER_STARTY=380

ENEMY_STARTY_MIN=50

ENEMY_STARTY_MAX=150

ENEMY_SPEEDX=4

ENEMY_SPEEDY=40

BULLET_SPEED_y=10

COLLISSION_DISTANCE=27

pygame.init()

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

background=pygame.image.load('enemy.png')

pygame.display.set_caption("Space Invader")

icon=pygame.image.load('ufo(2).png')

pygame.display.set_icon(icon)

playerImage=pygame.image.load("player.png")

playerx=PLAYER_STARTX

playery=PLAYER_STARTX

playerx_change=0

enemyImg = []

enemyx = []

enemyy = []

enemyx_change = []

enemyy_change = []

enemy_number = 6

for _i in range(enemy_number):
    
    enemyImg.append(pygame.image.load('enemy.png'))
    
    enemyx.append(random.randint(0,SCREEN_WIDTH - 64))
   
    enemyy.append(random.randint(ENEMY_STARTY_MIN,ENEMY_STARTY_MAX))
    
    enemyx_change.append(ENEMY_SPEEDX)
    
    enemyy_change.append(ENEMY_SPEEDX)
    
    enemyy_change.append(ENEMY_SPEEDY)
    
    bulletImg = pygame.image.load('bullet.png')
    
    bulletX = 0
    
    bulletY = PLAYER_STARTY
    
    bulletX_change = 0
    
    bulletY_change = BULLET_SPEED_y
    
    bullet_state = "ready"