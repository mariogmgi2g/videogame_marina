import pygame

# Dimensiones del spritesheet 640x256 (anchoxalto)
 
class SpriteSheet:
    """Función que selecciona el sprite adecuado de spritesheet"""
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        width = self.sprite_sheet.get_width()
        tamanio = self.sprite_sheet.get_size()
        #print(f"SPRITE SHEET| Tamaño: {tamanio}, anchura: {width}")
    
    def get_sprite(self, x, y, w, h):
        """Función que escoge el sprite de la spritesheet
        w y h son las dimensiones del sprite individual, mientras que x e y es
        donde se encuentran en el spritesheet tomando como referencia el punto
        (0, 0) la esquina superior izquierda relativa"""
        sprite = pygame.Surface((w, h))
        # Devuelve la imagen que queremos del sprite según la posición y 
        # las dimentsiones y las pinta en el canvas
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        width = sprite.get_width()
        tamanio = sprite.get_size()
        #print(f"SPRITE| Tamaño: {tamanio}, anchura: {width}")
        return sprite
    
    # def parse_sprite(self, name):


####
