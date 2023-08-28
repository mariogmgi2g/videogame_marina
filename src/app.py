from config import cfg_item
from render import SpriteSheet

import os
import time
import pygame

class App : 
    def __init__ (self, canvas, window, running):

        ruta_imagen = os.path.join(
            os.path.dirname(__file__), '../data/assets/images/walking_animation.png')
        h, w = cfg_item("image", "rects_size")
        my_spritesheet = SpriteSheet(ruta_imagen)

        # Como de ancho el spritesheet mide 640 pixeles, se va desplazando la anchura 
        # proporcionalmente
        chica_derecha = [my_spritesheet.get_sprite(w*i, 0, w, h) for i in range(1,10)]
        chica_izquierda = [my_spritesheet.get_sprite(w*i, h, w, h-2) for i in range(1,10)]
        chica_reposo_derecha = [my_spritesheet.get_sprite(0, 0, w, h)]
        chica_reposo_izquierda = [my_spritesheet.get_sprite(0, h, w, h-2)]
        #chica_salto = [my_spritesheet.get_sprite(0, 0, w, h) for i in range(1,10)]
        self.chica_movimientos = {0: chica_derecha, 1: chica_izquierda, 2: chica_reposo_derecha, 3: chica_reposo_izquierda}
        # 0: movimiento derecha; 1: movimiento izquierda; 2: frame reposo derecha; 3: frame reposo izquierda

        self.sprite1 = my_spritesheet.get_sprite(0, 0, w, h)
        # sprite1 = my_spritesheet.get_sprite(0, 0, 640, 256)

        self.index = 0
        self.direccion = 0
        self.desplazamiento_x = 32
        self.loc_x = 0
        self.desplazamiento_y = -18
        self.loc_y = (480-128)
        self.inicio = True
        self.evento = False
        self.direccion_anterior = 0
        self.canvas = canvas
        self.window = window
        self.running = running

    def run(self):
        while self.running:
            if self.inicio : 
                while (not self.evento) :
                    if ((self.loc_x + self.desplazamiento_x <= (640-64)) & (self.direccion_anterior == 0)) | ((self.loc_x == 0) & (self.direccion_anterior == 1)) :
                        self.direccion = 0
                        self.loc_x += self.desplazamiento_x
                        self.loc_y += self.desplazamiento_y
                        self.index = (self.index + 1) % len(self.chica_movimientos[0])
                    else:
                        if ((self.loc_x - self.desplazamiento_x >= 0) & (self.direccion_anterior == 1)) | ((self.loc_x == (640-64)) & (self.direccion_anterior == 0)):
                            self.direccion = 1
                            self.loc_x -= self.desplazamiento_x
                            self.loc_y -= self.desplazamiento_y
                            self.index = (self.index + 1) % len(self.chica_movimientos[1])

                    
                    self.direccion_anterior = self.direccion

                    print("evento_devuelto:")
                    print(pygame.event.peek([pygame.KEYDOWN, pygame.QUIT]))
                    self.evento = (pygame.event.peek([pygame.KEYDOWN, pygame.QUIT]))
                    print("iteracion: {}".format(str(self.index)))
                    self.canvas.fill((0, 0, 0))
                    # La segunda dupla de valores del blit controla dónde se materializa el
                    # sprite con referencia del canvas, siendo su esquina superior izquierda
                    # el punto 0, 0
                    self.canvas.blit(self.chica_movimientos[self.direccion][self.index], (self.loc_x, self.loc_y))
                    self.window.blit(self.canvas, (0,0))
                    pygame.display.update() 
                    time.sleep(0.5)
                        
            self.inicio = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.direccion = 0
                        if (self.loc_x + self.desplazamiento_x <= (640-64)) & ((self.direccion_anterior == self.direccion) | (self.direccion_anterior == 3)):
                            self.loc_x += self.desplazamiento_x
                            self.index = (self.index + 1) % len(self.chica_derecha)
                        else:
                            self.index = 0
                            self.direccion = 3

                    if event.key == pygame.K_LEFT:              
                            self.direccion = 1
                            if (self.loc_x - self.desplazamiento_x >= 0) & ((self.direccion_anterior == self.direccion) | (self.direccion_anterior == 2)):
                                self.loc_x -= self.desplazamiento_x
                                self.index = (self.index + 1) % len(self.chica_izquierda)
                            else:
                                self.index = 0
                                self.direccion = 2

                self.direccion_anterior = self.direccion


            self.canvas.fill((0, 0, 0))
            # La segunda dupla de valores del blit controla dónde se materializa el
            # sprite con referencia del canvas, siendo su esquina superior izquierda
            # el punto 0, 0
            self.canvas.blit(self.chica_movimientos[self.direccion][self.index], (self.loc_x, self.loc_y))
            self.window.blit(self.canvas, (0, 256))
            pygame.display.update() 