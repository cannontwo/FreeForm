import pygame
import entity
import main


class EventHandler():
    """Class responsible for reacting to events according to event type"""
    def __init__(self, pool):
        self.pool = pool

    def handle(self, events):
        test_surf = pygame.image.load('res/circle.png').convert_alpha()
        mouse_down = False
        for event in events:

            if event.type == pygame.QUIT:
                main.clean_exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main.clean_exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = [event.pos[0] - test_surf.get_width()/2, event.pos[1] - test_surf.get_height()/2]
                temp = entity.Entity(test_surf, pos)
                self.pool.add_entity(temp)
                self.pool.set_selected(temp)
                mouse_down = True

            elif event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    self.pool.get_selected().pos = [event.pos[0] - test_surf.get_width()/2, event.pos[1] - test_surf.get_height()/2]

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
                self.pool.remove_entity(self.pool.get_selected())
                self.pool.set_selected(None)