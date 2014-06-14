import pygame

import entity
import main


class EventHandler():
    """Class responsible for reacting to events according to event type"""
    def __init__(self, pool, box):
        pygame.key.set_repeat(250, 30)
        self.pool = pool
        self.box = box
        self.selected = []

    def handle(self, events):
        test_surf = pygame.image.load('res/circle.png').convert_alpha()

        for event in events:

            if event.type == pygame.QUIT:
                self.pool.save()
                main.clean_exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pool.save()
                    main.clean_exit()
                elif event.key == pygame.K_SPACE and event.mod == pygame.KMOD_LCTRL:
                    self.pool.get_selected().radius += 10
                elif event.key == pygame.K_z and event.mod == pygame.KMOD_LCTRL and self.pool.get_selected().radius > 10:
                    self.pool.get_selected().radius -= 10
                elif event.key == pygame.K_s and event.mod == pygame.KMOD_LCTRL:
                    self.pool.save()
                elif event.key == pygame.K_l and event.mod == pygame.KMOD_LCTRL:
                    self.pool.load()
                elif event.key == pygame.K_DELETE and self.pool.get_selected():
                    self.pool.remove_entity(self.pool.get_selected())
                    self.pool.set_selected(None)
                elif event.key == pygame.K_TAB:
                    self.box.tab_switch()
                elif event.key <= 127:
                    if self.pool.get_selected():
                        self.box.add_char(event.key)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for temp_entity in sorted(self.pool.get_entities(), key=lambda temp_ent: temp_ent.z_val, reverse=True):
                        if pygame.Rect(temp_entity.pos, (temp_entity.radius * 2, temp_entity.radius * 2)).collidepoint(event.pos):
                            if pygame.key.get_mods() & pygame.KMOD_LSHIFT and self.pool.get_selected():
                                self.selected.append(temp_entity)
                                self.pool.connect(self.pool.get_selected(), temp_entity)
                                self.pool.set_selected(temp_entity)
                            else:
                                self.pool.set_selected(temp_entity)
                                self.selected = []
                            return
                    if self.pool.get_selected():
                        self.box.add_char(pygame.K_RETURN)
                        self.pool.set_selected(None)
                if event.button == 3:
                    for temp_entity in sorted(self.pool.get_entities(), key=lambda temp_ent: temp_ent.z_val, reverse=True):
                        if pygame.Rect(temp_entity.pos, (temp_entity.radius * 2, temp_entity.radius * 2)).collidepoint(event.pos):
                            temp_entity.connections = []
                            self.pool.set_selected(temp_entity)

            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:
                    if self.pool.get_selected():
                        for ent in self.pool.get_selected().connections:
                            diff = [self.pool.get_selected().center[i] - ent.center[i] for i in range(len(ent.center))]
                            ent.center = [event.pos[i] - diff[i] for i in range(len(ent.center))]
                        self.pool.get_selected().center = event.pos

                    else:
                        center = event.pos
                        temp = entity.Entity(test_surf, center)
                        self.pool.add_entity(temp)
                        self.pool.set_selected(temp)