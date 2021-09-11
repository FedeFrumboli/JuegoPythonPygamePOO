import pygame
from pygame.locals import *
import sys
import time
from player import *
from enemigo import *
from enemigo2 import *
from background import *


# Inicio pygame
pygame.init()

# Ventana
size = (800,800)
DISPLAYSURF = pygame.display.set_mode(size)
#DISPLAYSURF.fill("WHITE")
pygame.display.set_caption("Juego")

# Creo objetos
background_nivel1 = Background()
player = Player(background_nivel1)
enemigo1 = Enemigo()
enemigo2 = EnemigoCarril()



# Creo grupos de sprites
enemigos = pygame.sprite.Group()
enemigos.add(enemigo1)
enemigos.add(enemigo2)

todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(player)
todos_los_sprites.add(enemigo1)
todos_los_sprites.add(enemigo2)



# Creo evento del juego (+1 para que tenga ID unica)
# aumentar_velocidad_enemigo = pygame.USEREVENT + 1
# Funcion de aumentar velocidad enemigo cada x milisegundos
#pygame.time.set_timer(aumentar_velocidad_enemigo, 10000)


#_____________________________________________________
# Inicio Loop del juego
while True:

    # Aplico background
    background_nivel1.update()
    background_nivel1.render(DISPLAYSURF)
    


    # Detecto colisiones entre player y enemigos
    if pygame.sprite.spritecollideany(player, enemigos):
        DISPLAYSURF.fill("BLACK")
        pygame.display.update()
        for entidades in todos_los_sprites:
            entidades.kill()
        time.sleep(1)
        pygame.quit()
        sys.exit()

    
    # Dibujo y muevo todos los sprites
    for entidades in todos_los_sprites:
        DISPLAYSURF.blit(entidades.image, entidades.rect)
        # Las entidades son todos los sprites y c/u tiene un metodo llamado move
        entidades.move()
    
    background_nivel1.move()

    #_____________________________________________________
    # Defino FPS
    FPS = pygame.time.Clock()
    FPS.tick(120)
    
    # Actualizo pantalla
    pygame.display.update()

    # Eventos del juego
    for event in pygame.event.get():

        # Evento aumentar velocidad enemigo
        #if event.type == aumentar_velocidad_enemigo:
            #enemigo1.velocidad += 1 

        # Evento salir del bucle (QUIT)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Fin loop del juego 
    #_____________________________________________________