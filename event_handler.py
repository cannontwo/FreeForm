import pygame

import entity
import main
import text_box


class EventHandler():
    """Class responsible for reacting to events according to event type"""
    def __init__(self, pool, box):
        pygame.key.set_repeat(250, 30)
        self.pool = pool
        self.box = box
        self.prev_mouse_down = 0

    def handle(self, events):
        test_surf = pygame.image.load('res/circle.png').convert_alpha()

        for event in events:

            if event.type == pygame.QUIT:
                main.clean_exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main.clean_exit()
                elif event.key == pygame.K_SPACE and event.mod == pygame.KMOD_LCTRL:
                    self.pool.get_selected().radius += 10
                elif event.key == pygame.K_z and event.mod == pygame.KMOD_LCTRL and self.pool.get_selected().radius > 10:
                    self.pool.get_selected().radius -= 10
                elif event.key == pygame.K_TAB:
                    text_box.TextBox.global_box.tab_switch()
                elif event.key <= 127:
                    if self.pool.get_selected():
                        self.box.add_char(event.key)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    for temp_entity in sorted(self.pool.get_entities(), key=lambda temp_ent: temp_ent.z_val, reverse=True):
                        if pygame.Rect(temp_entity.pos, (temp_entity.radius * 2, temp_entity.radius * 2)).collidepoint(event.pos):
                            self.pool.set_selected(temp_entity)
                            return
                    if self.pool.get_selected():
                        text_box.TextBox.global_box.add_char(pygame.K_RETURN)
                        self.pool.set_selected(None)

            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:
                    if self.pool.get_selected():
                        self.pool.get_selected().center = event.pos
                        self.pool.get_selected().pos = [event.pos[0] - test_surf.get_width()/2, event.pos[1] - test_surf.get_height()/2]
                    else:
                        center = event.pos
                        temp = entity.Entity(test_surf, center)
                        self.pool.add_entity(temp)
                        self.pool.set_selected(temp)

            elif event.type == pygame.MOUSEBUTTONUP:
                print "Button released"
