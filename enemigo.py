import pygame
from pygame.locals import *
import os
import random

# Directorio de imagenes
filepath = os.path.dirname(os.path.abspath(__file__))

class Enemigo(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(filepath + "\\img\\" "enemigoVerde.png"))
        self.surf = pygame.Surface((23,40))
        self.rect = self.surf.get_rect(center=(random.randrange(360,388,27),-40))

        self.velocidad = 1
        
    def move(self):
        self.rect.move_ip(0,self.velocidad)
        if (self.rect.top > 800):
            self.rect.top = 0
            self.rect.center = (random.randrange(360,388,27), -40)

        pressed_keys = pygame.key.get_pressed()

        if self.velocidad < 8:
            if pressed_keys[K_UP]:
                self.velocidad += 0.025
                
        if self.velocidad > 1:
            if pressed_keys[K_DOWN]:
                self.velocidad -= 0.05
                # Control para que el enemigo no se frene por completo
                if self.velocidad <1:
                    self.velocidad = 1
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)