#!/usr/bin/python
import event_handler
import gui
import pool

__author__ = 'cannon'

import pygame
import sys

def run(width=1200, height=800):
    pygame.init()

    draw = False

    screen = pygame.display.set_mode((width, height))
    menu = pygame.Surface((width*.075, height*.4))
    circle = pygame.image.load('res/circle.png').convert_alpha()

    clock = pygame.time.Clock()

    while 1:
        ####################################
        #CONSTRUCTION AREA                 #
        ####################################
        screen.fill((137, 207, 240))
        event_handler.handle(pygame.event.get())
        for entity in pool.get_entities():
            entity.update(clock.tick())
            entity.render(screen)
        gui.render(screen)
        #####################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                draw = True
                pos = (event.pos[0] - circle.get_width()/2, event.pos[1] - circle.get_height()/2)
            elif event.type == pygame.MOUSEMOTION:
                pos = (event.pos[0] - circle.get_width()/2, event.pos[1] - circle.get_height()/2)
            elif event.type == pygame.MOUSEBUTTONUP:
                draw = False

        menu.fill((192, 192, 192))
        pygame.draw.rect(menu, (0, 0, 0), pygame.Rect(0, 0, menu.get_width(), menu.get_height()), 5)
        menu.set_alpha(150)

        screen.fill((137, 207, 240))
        if draw:
            screen.blit(circle, pos)
        screen.blit(menu, (0, 0))

        pygame.display.flip()

if __name__ == "__main__":
    if len(sys.argv) == 3:
        run(int(sys.argv[1]), int(sys.argv[2]))
    else:
        run()