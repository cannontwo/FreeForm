import pygame


class Gui():
    """Class to handle state and rendering of gui"""

    def __init__(self, width, height):
        self.menu = pygame.Surface((width*.05, height*.4))
        self.menu_color = (192, 192, 192)
        self.menu.fill(self.menu_color)
        pygame.draw.rect(self.menu, (0, 0, 0), pygame.Rect(0, 0, self.menu.get_width(), self.menu.get_height()), 5)

        home_surf = pygame.image.load('res/home.png').convert_alpha()
        shapes_surf = pygame.image.load('res/shapes.png').convert_alpha()
        save_surf = pygame.image.load('res/save.png').convert_alpha()
        open_surf = pygame.image.load('res/open.png').convert_alpha()
        settings_surf = pygame.image.load('res/settings.png').convert_alpha()

        self.menu_partials = [home_surf, shapes_surf, save_surf, open_surf, settings_surf]
        for i in range(0, 5):
            trans = pygame.transform.scale(self.menu_partials[i], (self.menu.get_rect().width, self.menu.get_rect().height / 5))
            self.menu.blit(trans, (0, i * trans.get_rect().height))

        #Variable to store string representing submenu currently open
        self.open = None

    def render(self, target_surf):
        assert isinstance(target_surf, pygame.Surface), "target_surf must be a Surface"
        self.menu.set_alpha(175)
        target_surf.blit(self.menu, (30,20))