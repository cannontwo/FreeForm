import pygame


class Entity():
    """Class used to represent different data objects, differences defined by type string. (Subclasses?)"""

    def __init__(self, surf, center, type="circle", radius=80):
        self.surf = surf
        self.center = center
        self.pos = [center[0] - radius, center[1] - radius]
        self.type = type
        self.radius = radius
        self.vel = [0.0, 0.0]
        self.acc = [0.0, 0.0]
        self.z_val = 0

    def update(self, delta):
        #Updates position
        self.pos = [self.center[0] - self.radius, self.center[1] - self.radius]
        modif = (float(delta) / float(1000))
        self.pos[0] = int(float(self.pos[0]) + float(self.vel[0]) * modif)
        self.pos[1] = int(float(self.pos[1]) + float(self.vel[1]) * modif)
        self.vel[0] = int(float(self.vel[0]) + float(self.acc[0]) * modif)
        self.vel[1] = int(float(self.vel[1]) + float(self.acc[1]) * modif)

    def render(self, target_surf):
        assert isinstance(target_surf, pygame.Surface), "target_surf must be a Surface"
        target_surf.blit(pygame.transform.scale(self.surf, (self.radius * 2, self.radius * 2)), self.pos)