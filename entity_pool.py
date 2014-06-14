import entity


class EntityPool():

    def __init__(self):
        self.entity_list = []
        self.selected = None

    def update(self, delta):
        for loc_entity in self.entity_list:
            loc_entity.update(delta)

    def render(self, target_surf):
        for loc_entity in self.entity_list:
            loc_entity.render(target_surf)
        if self.selected:
            #TODO Once radius scaling is implemented, add code to highlight selected element
            return

    def get_entities(self):
        return self.entity_list

    def add_entity(self, thing):
        assert isinstance(thing, entity.Entity), "You may only add entity objects to the pool"
        self.entity_list.append(thing)

    def remove_entity(self, thing):
        self.entity_list.remove(thing)

    def set_selected(self, thing):
        self.selected = thing

    def get_selected(self):
        return self.selected