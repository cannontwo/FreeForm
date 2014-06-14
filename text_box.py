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
        self.editing_title = True
        TextBox.global_box = self

    def render(self):
        self.display_box(string.join(self.current_string, ""))

    def display_box(self, message):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)

        if self.pool.get_selected():
            if self.editing_title:
                self.screen.blit(self.font.render("Title: " + message + "|", 1, (255, 255, 255)), self.rect.topleft)
                self.screen.blit(self.font.render("Text: " + self.pool.get_selected().text, 1, (255, 255, 255)), (self.rect.topleft[0] + self.screen.get_rect().width / 2, self.rect.topleft[1]))
            else:
                self.screen.blit(self.font.render("Title: " + self.pool.get_selected().title, 1, (255, 255, 255)), self.rect.topleft)
                self.screen.blit(self.font.render("Text: " + message + "|", 1, (255, 255, 255)), (self.rect.topleft[0] + self.screen.get_rect().width / 2, self.rect.topleft[1]))

    def add_char(self, inkey):
        if inkey == pygame.K_BACKSPACE:
            self.current_string = self.current_string[0:-1]
        elif inkey == pygame.K_RETURN and self.pool.get_selected():
            self.tab_switch()
        elif inkey <= 127:
            self.current_string.append(chr(inkey))

    def tab_switch(self):
        if self.editing_title:
            self.pool.get_selected().title = string.join(self.current_string, "")
            self.current_string = list(self.pool.get_selected().text)
        else:
            self.pool.get_selected().text = string.join(self.current_string, "")
            self.current_string = list(self.pool.get_selected().title)
        self.editing_title = not self.editing_title

    def set_string(self, instring):
        self.current_string = list(instring)