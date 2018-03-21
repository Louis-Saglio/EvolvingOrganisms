import pygame


class PygameOrganism:

    def __init__(self, organism, screen):
        self.size = 1000, 1000
        self.screen = screen
        self.organism = organism
        self.image = pygame.transform.scale(pygame.image.load("ball.gif").convert_alpha(), self.size)
        self.rect = self.image.get_rect()

    def get_gui_coord(self):
        return self.organism.x * self.screen.get_width(), self.organism.y * self.screen.get_height()

    def draw(self):
        self.screen.blit(self.image, self.get_gui_coord())
