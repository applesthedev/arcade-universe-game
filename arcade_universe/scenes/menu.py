import pygame
from .base import Scene
from .snake import Snake
from .guess import GuessGame
from .placeholder import Placeholder


class Tile:
    def __init__(self, x, y, w, h, text, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.action = action
        self.hovered = False

    def update(self, mouse):
        self.hovered = self.rect.collidepoint(mouse)

    def draw(self, screen, font):
        color = (80, 80, 120) if self.hovered else (40, 40, 60)

        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        pygame.draw.rect(screen, (120, 120, 160), self.rect, 2, border_radius=10)

        txt = font.render(self.text, True, (255, 255, 255))
        screen.blit(txt, txt.get_rect(center=self.rect.center))

    def click(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.hovered


class Menu(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.font = pygame.font.SysFont("arialblack", 26)

        self.tiles = [
            Tile(200, 120, 400, 60, "Snake", self.start_snake),
            Tile(200, 200, 400, 60, "Guess Game", self.start_guess),
            Tile(200, 280, 400, 60, "Tic Tac Toe (Coming Soon)", self.ttt),
            Tile(200, 360, 400, 60, "Breakout (Coming Soon)", self.breakout),
            Tile(200, 440, 400, 60, "Flappy Bird (Coming Soon)", self.flappy),
        ]

    def start_snake(self):
        self.game.change_scene(Snake(self.game))

    def start_guess(self):
        self.game.change_scene(GuessGame(self.game))

    def ttt(self):
        self.game.change_scene(Placeholder(self.game, "Tic Tac Toe"))

    def breakout(self):
        self.game.change_scene(Placeholder(self.game, "Breakout"))

    def flappy(self):
        self.game.change_scene(Placeholder(self.game, "Flappy Bird"))

    def handle_event(self, event):
        for t in self.tiles:
            if t.click(event):
                t.action()

    def update(self, dt):
        mouse = pygame.mouse.get_pos()
        for t in self.tiles:
            t.update(mouse)

    def draw(self, screen):
        screen.fill((15, 15, 25))

        title = self.font.render("ARCADE UNIVERSE v0.1", True, (255, 255, 255))
        screen.blit(title, title.get_rect(center=(400, 50)))

        for t in self.tiles:
            t.draw(screen, self.font)