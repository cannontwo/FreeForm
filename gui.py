import pygame


class Gui():
    """Class to handle state and rendering of gui"""

    def __init__(self, width, height):
        self.menu = pygame.Surface((width*.075, height*.4))
        self.menu_color = (192, 192, 192)

        #Variable to store string representing submenu currently open
        self.open = None

    def render(self, target_surf):
        assert isinstance(target_surf, pygame.Surface), "target_surf must be a Surface"
        self.menu.fill((192, 192, 192))
        pygame.draw.rect(self.menu, (0, 0, 0), pygame.Rect(0, 0, self.menu.get_width(), self.menu.get_height()), 5)
        self.menu.set_alpha(150)
        target_surf.blit(self.menu, (0,0))