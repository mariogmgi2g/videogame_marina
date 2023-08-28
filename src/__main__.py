from app import App
from config import cfg_item

import pygame


if __name__ == '__main__':
    pygame.init()
    DISPLAY_W, DISPLAY_H = cfg_item("game", "screen_size")
    canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
    window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    running = True
    app = App(canvas, window, running) 
    app.run()