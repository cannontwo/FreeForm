import pygame

import entity
import text_box


class EntityPool():
    """Objects of this class keep track of collections of entities"""

    def __init__(self):
        self.entity_list = []
        self.selected = None
        self.master_z = 1

    def update(self, delta):
        for loc_entity in self.entity_list:
            loc_entity.update(delta)

    def render(self, target_surf):
        for loc_entity in self.entity_list:
            loc_entity.render(target_surf)
        if self.selected:
            pygame.draw.circle(target_surf, (255, 102, 0), self.selected.center, self.selected.radius + 2)
            return

    def get_entities(self):
        return self.entity_list

    def add_entity(self, thing):
        assert isinstance(thing, entity.Entity), "You may only add entity objects to the pool"
        thing.z_val = self.master_z
        self.entity_list.append(thing)

    def remove_entity(self, thing):
        self.entity_list.remove(thing)

    def set_selected(self, thing):
        if self.selected:
            text_box.TextBox.global_box.set_string("")
        if thing:
            thing.z_val = self.master_z
            self.master_z += 1
            text_box.TextBox.global_box.set_string(thing.text)
        self.selected = thing

    def get_selected(self):
        return self.selected