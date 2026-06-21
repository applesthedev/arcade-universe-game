import pygame
from .base import Scene


class Placeholder(Scene):
    def __init__(self, game, text):
        super().__init__(game)
        self.text = text
        self.font = pygame.font.SysFont("arialblack", 40)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.change_scene(self.game.menu_class(self.game))

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill((10, 10, 20))

        txt = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(txt, txt.get_rect(center=(400, 300)))