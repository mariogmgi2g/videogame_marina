
from config import cfg_item
from render import SpriteSheet
import os
import time
import pygame


if __name__ == '__main__':
    pygame.init()
    DISPLAY_W, DISPLAY_H = cfg_item("game", "screen_size")
    canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
    window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    running = True

ruta_imagen = os.path.join(
    os.path.dirname(__file__), 'assets/images/walking_animation.png')
h, w = cfg_item("image", "rects_size")
my_spritesheet = SpriteSheet(ruta_imagen)

# Como de ancho el spritesheet mide 640 pixeles, se va desplazando la anchura 
# proporcionalmente
chica_derecha = [my_spritesheet.get_sprite(w*i, 0, w, h) for i in range(1,10)]
chica_izquierda = [my_spritesheet.get_sprite(w*i, h, w, h-2) for i in range(1,10)]
chica_reposo_derecha = [my_spritesheet.get_sprite(0, 0, w, h)]
chica_reposo_izquierda = [my_spritesheet.get_sprite(0, h, w, h-2)]
#chica_salto = [my_spritesheet.get_sprite(0, 0, w, h) for i in range(1,10)]
chica_movimientos = {0: chica_derecha, 1: chica_izquierda, 2: chica_reposo_derecha, 3: chica_reposo_izquierda}
# 0: movimiento derecha; 1: movimiento izquierda; 2: frame reposo derecha; 3: frame reposo izquierda

sprite1 = my_spritesheet.get_sprite(0, 0, w, h)
# sprite1 = my_spritesheet.get_sprite(0, 0, 640, 256)

index = 0
direccion = 0
desplazamiento_x = 32
loc_x = 0
desplazamiento_y = -18
loc_y = (480-128)
inicio = True
evento = False
direccion_anterior = 0

while running:
    if inicio : 
        while (not evento) :
            if ((loc_x + desplazamiento_x <= (640-64)) & (direccion_anterior == 0)) | ((loc_x == 0) & (direccion_anterior == 1)) :
                direccion = 0
                loc_x += desplazamiento_x
                loc_y += desplazamiento_y
                index = (index + 1) % len(chica_derecha)
            else:
                if ((loc_x - desplazamiento_x >= 0) & (direccion_anterior == 1)) | ((loc_x == (640-64)) & (direccion_anterior == 0)):
                    direccion = 1
                    loc_x -= desplazamiento_x
                    loc_y -= desplazamiento_y
                    index = (index + 1) % len(chica_izquierda)

            
            direccion_anterior = direccion

            print("evento_devuelto:")
            print(pygame.event.peek([pygame.KEYDOWN, pygame.QUIT]))
            evento = (pygame.event.peek([pygame.KEYDOWN, pygame.QUIT]))
            print("iteracion: {}".format(str(index)))
            canvas.fill((0, 0, 0))
            # La segunda dupla de valores del blit controla dónde se materializa el
            # sprite con referencia del canvas, siendo su esquina superior izquierda
            # el punto 0, 0
            canvas.blit(chica_movimientos[direccion][index], (loc_x, loc_y))
            window.blit(canvas, (0,0))
            pygame.display.update() 
            time.sleep(0.5)
                   
    inicio = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direccion = 0
                if (loc_x + desplazamiento_x <= (640-64)) & ((direccion_anterior == direccion) | (direccion_anterior == 3)):
                    loc_x += desplazamiento_x
                    index = (index + 1) % len(chica_derecha)
                else:
                    index = 0
                    direccion = 3

            if event.key == pygame.K_LEFT:              
                    direccion = 1
                    if (loc_x - desplazamiento_x >= 0) & ((direccion_anterior == direccion) | (direccion_anterior == 2)):
                        loc_x -= desplazamiento_x
                        index = (index + 1) % len(chica_izquierda)
                    else:
                        index = 0
                        direccion = 2

        direccion_anterior = direccion


    canvas.fill((0, 0, 0))
    # La segunda dupla de valores del blit controla dónde se materializa el
    # sprite con referencia del canvas, siendo su esquina superior izquierda
    # el punto 0, 0
    canvas.blit(chica_movimientos[direccion][index], (loc_x, loc_y))
    window.blit(canvas, (0, 256))
    pygame.display.update() 