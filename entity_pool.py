import entity


class EntityPool():

    def __init__(self):
        self.entity_list = []
        self.selected = None

    def get_entities(self):
        return self.entity_list

    def add_entity(self, thing):
        assert isinstance(thing, entity.Entity), "You may only add entity objects to the pool"
        self.entity_list.append(thing)
        print "entity added"

    def remove_entity(self, thing):
        self.entity_list.remove(thing)
        print "entity removed"

    def set_selected(self, thing):
        self.selected = thing

    def get_selected(self):
        return self.selected