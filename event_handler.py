import pygame

import entity
import main


class EventHandler():
    """Class responsible for reacting to events according to event type"""
    def __init__(self, pool):
        pygame.key.set_repeat(250, 30)
        self.pool = pool
        self.mouse_down = False

    def handle(self, events):
        test_surf = pygame.image.load('res/circle.png').convert_alpha()

        for event in events:

            if event.type == pygame.QUIT:
                main.clean_exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main.clean_exit()
                elif event.key == pygame.K_SPACE:
                    self.pool.get_selected().radius += 10
                elif event.key == pygame.K_z and self.pool.get_selected().radius > 10:
                    self.pool.get_selected().radius -= 10

            elif event.type == pygame.MOUSEBUTTONDOWN:
                center = event.pos
                temp = entity.Entity(test_surf, center)
                self.pool.add_entity(temp)
                self.pool.set_selected(temp)
                self.mouse_down = True

            elif event.type == pygame.MOUSEMOTION:
                if self.mouse_down:
                    self.pool.get_selected().center = event.pos
                    self.pool.get_selected().pos = [event.pos[0] - test_surf.get_width()/2, event.pos[1] - test_surf.get_height()/2]

            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_down = False
                # self.pool.remove_entity(self.pool.get_selected())
                # self.pool.set_selected(None)