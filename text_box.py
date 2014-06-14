import pygameimport stringclass TextBox():    global_box = None    def __init__(self, screen, pool):        pygame.font.init()        self.font = pygame.font.Font(None, 30)        self.width = 1920        self.height = 100        self.screen = screen        self.selected = None        self.rect = pygame.Rect(0, 980, self.width, self.height)        self.pool = pool        self.current_string = []        self.editing_title = True        TextBox.global_box = self    def render(self):        self.selected = self.pool.get_selected()        if self.selected:            trans = self.selected.transformed_surf.get_rect()            self.rect = pygame.Rect(trans.bottomleft, (trans.width, trans.height))            self.rect.centerx = self.selected.center[0]            self.rect.top = self.selected.center[1] + self.selected.radius        self.display_box(string.join(self.current_string, ""))    def display_box(self, message):        xpos = 5        ypos_ti = 5        ypos_te = (self.rect.height / 2) + 5        if self.pool.get_selected():            base = pygame.Surface((self.rect.width, self.rect.height))            pygame.draw.rect(base, (0, 0, 0), self.rect)            base.set_alpha(150)            if self.editing_title:                surf_ti = self.font.render("Title: " + message + "|", 1, (255, 255, 255))                surf_te = self.font.render("Text: " + self.selected.text, 1, (255, 255, 255))            else:                surf_ti = self.font.render("Title: " + self.pool.get_selected().title, 1, (255, 255, 255))                surf_te = self.font.render("Text: " + message + "|", 1, (255, 255, 255))            base.blit(surf_ti, (xpos, ypos_ti))            base.blit(surf_te, (xpos, ypos_te))            pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 3)            self.screen.blit(base, self.rect)    def add_char(self, inkey):        if inkey == pygame.K_BACKSPACE:            self.current_string = self.current_string[0:-1]        elif inkey == pygame.K_RETURN and self.pool.get_selected():            self.save()        elif inkey <= 127:            self.current_string.append(chr(inkey))    def tab_switch(self):        if self.editing_title:            self.pool.get_selected().title = string.join(self.current_string, "")            self.current_string = list(self.pool.get_selected().text)        else:            self.pool.get_selected().text = string.join(self.current_string, "")            self.current_string = list(self.pool.get_selected().title)        self.editing_title = not self.editing_title    def save(self):        if self.editing_title:            self.pool.get_selected().title = string.join(self.current_string, "")        else:            self.pool.get_selected().text = string.join(self.current_string, "")    def set_string(self, instring):        self.current_string = list(instring)