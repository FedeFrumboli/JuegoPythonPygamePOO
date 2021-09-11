import pygame
from pygame.locals import *
import os

# Directorio de imagenes
filepath = os.path.dirname(os.path.abspath(__file__))

class Background():
    
    def __init__(self):
        self.bgimage = pygame.image.load(os.path.join(filepath + "\\img\\" "nivel1.jpg"))
        self.rectBGimg = self.bgimage.get_rect()
        #Posicion inicial de los fondos consecutivos
        self.bgY1 = -self.rectBGimg.height + 800
        self.bgX1 = 0
        self.bgY2 = -(2*self.rectBGimg.height) + 800
        self.bgX2 = 0
        # Velocidad inicial
        self.velocidad = 0
        # Medidas pista laterales
        self.lateralIzquierdo = 345
        self.lateralDerecho = 468

    def update(self):
        self.bgY1 += self.velocidad
        self.bgY2 += self.velocidad  
        if self.bgY1 >= 800:
            self.bgY1 = self.bgY2 - self.rectBGimg.height
        if self.bgY2 >= 800:
            self.bgY2 = self.bgY1 - self.rectBGimg.height
        

    def render(self, DISPLAYSURF):
        DISPLAYSURF.blit(self.bgimage, (self.bgX1, self.bgY1))
        DISPLAYSURF.blit(self.bgimage, (self.bgX2, self.bgY2))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.velocidad < 7:
            if pressed_keys[K_UP]:
                self.velocidad += 0.025
        if self.velocidad > 0:
            if pressed_keys[K_DOWN]:
                self.velocidad -= 0.05
                # Control para que no se mueva el fondo solo
                if self.velocidad < 0:
                    self.velocidad = 0

