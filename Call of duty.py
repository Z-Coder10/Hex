import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT =pygame.USEREVENT + 2
RED = pygame.Color('blue')
BLUE = pygame.Color('blue')
GREEN = pygame.Color('green')

GOLD = pygame.Color('gold')
Magenta = pygame.Color('magenta')
TURQUOISE = pygame.Color('Turquoise')
ORANGE = pygame.Color('Orange')

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
          super().__init__()
          self.image = pygame.Surface((width,height))
          self.image.fill(color)
          self.rect = self.image.get_rect()
          self.rect.x = random.randint(0,800 - width)
          self.rect.y = random.randint(0,600 - height)
          self.color = color
          self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
          
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <=0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <=0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
            if boundary_hit:
                pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT, {'sprite': self}))
                pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    def change_color(self):
        self.image.fill(random.choice([BLUE, RED, GREEN]))
        
    def change_background_color(self):
        global bg_color 
        bg_coloR = random.choice([GOLD, Magenta,TURQUOISE,ORANGE])
           