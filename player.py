import pygame
from pygame.locals import *
import os
import time

# Directorio de imagenes
filepath = os.path.dirname(os.path.abspath(__file__))

class Player(pygame.sprite.Sprite):
    
    def __init__(self, nivel):
        super().__init__()
        self.image = pygame.image.load(os.path.join(filepath + "\\img\\" "miAuto.png"))
        self.surf = pygame.Surface((21,41))
        self.rect = self.surf.get_rect(center=(420,700))

        self.velocidad = -1
        self.velocidadFreno = 1
        self.velocidadDireccion = 1

        self.nivel = nivel
        

    def move(self):
        
        pressed_keys = pygame.key.get_pressed()
        self.image = pygame.image.load(os.path.join(filepath + "\\img\\" "miAuto.png"))
        
        
        if pressed_keys[K_UP]:
            if self.rect.top >= 600:
                self.rect.move_ip(0,self.velocidad)

        if pressed_keys[K_DOWN]:
            self.image = pygame.image.load(os.path.join(filepath + "\\img\\" "miAutoFreno.png"))
            if self.rect.bottom <= 700:
                self.rect.move_ip(0,self.velocidadFreno)
     
        if self.rect.left > self.nivel.lateralIzquierdo:
            if pressed_keys[K_LEFT]:
                self.image = pygame.image.load(os.path.join(filepath + "\\img\\" "miAutoIzq.png"))
                self.rect.move_ip(-self.velocidadDireccion,0)      
        
        if self.rect.right < self.nivel.lateralDerecho:
            if pressed_keys[K_RIGHT]:
                self.image = pygame.image.load(os.path.join(filepath + "\\img\\" "miAutoDer.png"))
                self.rect.move_ip(self.velocidadDireccion,0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
