import pygame


class Entity():
    """Class used to represent different data objects, differences defined by type string. (Subclasses?)"""

    def __init__(self, surf, pos, type="circle", radius=5):
        self.surf = surf
        self.pos = pos
        self.type = type
        self.radius = radius
        self.vel = [0.0, 0.0]
        self.acc = [0.0, 0.0]

        assert isinstance(pos, list), "Pos must be a list of len >= 2"

    def update(self, delta):
        #Updates position
        modif = (float(delta) / float(1000))
        self.pos[0] = int(float(self.pos[0]) + float(self.vel[0]) * modif)
        self.pos[1] = int(float(self.pos[1]) + float(self.vel[1]) * modif)
        self.vel[0] = int(float(self.vel[0]) + float(self.acc[0]) * modif)
        self.vel[1] = int(float(self.vel[1]) + float(self.acc[1]) * modif)

    def render(self, target_surf):
        assert isinstance(target_surf, pygame.Surface), "target_surf must be a Surface"
        #Add code here to apply appropriate transform for radius
        target_surf.blit(self.surf, self.pos)

    #TODO Add methods to allow for increasing and decreasing radius
