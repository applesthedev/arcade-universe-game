import pygame
import random
from .base import Scene


class GuessGame(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.number = random.randint(1, 100)
        self.input_text = ""
        self.message = "Guess 1-100"

        self.font = pygame.font.SysFont("arialblack", 40)
        self.small = pygame.font.SysFont("arial", 24)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                self.game.change_scene(self.game.menu_class(self.game))

            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]

            elif event.key == pygame.K_RETURN:
                if self.input_text.isdigit():
                    guess = int(self.input_text)

                    if guess < self.number:
                        self.message = "Too Low"
                    elif guess > self.number:
                        self.message = "Too High"
                    else:
                        self.message = "Correct!"

                self.input_text = ""

            elif event.unicode.isdigit():
                self.input_text += event.unicode

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill((20, 20, 30))

        title = self.font.render("GUESS GAME", True, (255, 255, 255))
        screen.blit(title, (200, 100))

        msg = self.small.render(self.message, True, (200, 200, 200))
        screen.blit(msg, (250, 200))

        inp = self.font.render(self.input_text, True, (255, 255, 255))
        screen.blit(inp, (320, 300))