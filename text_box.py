import pygame
import string


class TextBox():
    global_box = None
    def __init__(self, screen, pool):
        pygame.font.init()
        self.font = pygame.font.Font(None, 40)
        self.editing = False
        self.width = 1920
        self.height = 100
        self.screen = screen
        self.rect = pygame.Rect(0, 980, self.width, self.height)
        self.pool = pool
        self.current_string = []
        TextBox.global_box = self

    def render(self):
        self.display_box(string.join(self.current_string, ""))

    def display_box(self, message):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)

        if len(message) != 0:
            self.screen.blit(self.font.render(message, 1, (255, 255, 255)), self.rect.topleft)

    def add_char(self, inkey):
        if inkey == pygame.K_BACKSPACE:
            self.current_string = self.current_string[0:-1]
        elif inkey == pygame.K_RETURN:
            self.pool.get_selected().text = string.join(self.current_string, "")
            self.pool.set_selected(None)
            self.current_string = []
        elif inkey <= 127:
            self.current_string.append(chr(inkey))

    def set_string(self, instring):
        self.current_string = list(instring)