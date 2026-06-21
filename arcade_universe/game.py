import pygame
import json
import os

from scenes.menu import Menu


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Arcade Universe v0.1")

        self.clock = pygame.time.Clock()
        self.running = True

        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        # save system
        self.save_file = os.path.join(self.base_dir, "data", "save.json")
        self.data = {
            "coins": 0,
            "snake_highscore": 0
        }
        self.load()

        self.scene = Menu(self)

        self.menu_class = Menu

    def load(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, "r") as f:
                self.data = json.load(f)

    def save(self):
        os.makedirs(os.path.dirname(self.save_file), exist_ok=True)
        with open(self.save_file, "w") as f:
            json.dump(self.data, f, indent=2)

    def change_scene(self, scene):
        self.scene = scene

    def run(self):
        while self.running:
            dt = self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.scene.handle_event(event)

            self.scene.update(dt)
            self.scene.draw(self.screen)

            pygame.display.flip()

        pygame.quit()