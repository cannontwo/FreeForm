__author__ = 'cannon'

class Entity:
    """Class used to represent different data objects, differences defined by type string. (Subclasses?)"""

    def __init__(self, surf, pos, type="circle", radius=5):
        self.surf = surf
        self.pos = pos
        self.type = type
        self.radius = radius
        self.vel = [0, 0]
        self.acc = [0, 0]

        assert isinstance(pos, list)

    def update(self, delta):
        #Updates position
        self.pos += self.vel * (float(delta) / float(1000))
        self.vel += self.acc * (float(delta) / float(1000))

    def render(self, target_surf):
        #Add code here to apply appropriate transform for radius
        target_surf.blit(self.surf, self.pos)

    #TODO Add methods to allow for increasing and decreasing radius
