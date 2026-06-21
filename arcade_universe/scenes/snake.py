import pygame
import random
from .base import Scene


class Snake(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.grid_w = 20
        self.grid_h = 15
        self.cell = 40

        self.reset()

        self.timer = 0
        self.speed = 120  # ms per move

        self.font = pygame.font.SysFont("arialblack", 50)
        self.small = pygame.font.SysFont("arial", 24)

    # -------------------------
    # RESET GAME
    # -------------------------
    def reset(self):
        self.body = [(5, 5)]
        self.dir = (1, 0)
        self.food = self.spawn_food()
        self.game_over = False

    def spawn_food(self):
        return (
            random.randint(0, self.grid_w - 1),
            random.randint(0, self.grid_h - 1)
        )

    # -------------------------
    # INPUT
    # -------------------------
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:

            # always go back to menu
            if event.key == pygame.K_ESCAPE:
                self.game.change_scene(self.game.menu_class(self.game))

            # restart ONLY when game over
            if self.game_over:
                if event.key == pygame.K_r:
                    self.reset()
                return

            # movement
            if event.key == pygame.K_UP and self.dir != (0, 1):
                self.dir = (0, -1)
            elif event.key == pygame.K_DOWN and self.dir != (0, -1):
                self.dir = (0, 1)
            elif event.key == pygame.K_LEFT and self.dir != (1, 0):
                self.dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and self.dir != (-1, 0):
                self.dir = (1, 0)

    # -------------------------
    # UPDATE
    # -------------------------
    def update(self, dt):
        if self.game_over:
            return

        self.timer += dt
        if self.timer < self.speed:
            return
        self.timer = 0

        head = self.body[0]
        new_head = (head[0] + self.dir[0], head[1] + self.dir[1])

        # -------------------------
        # WALL COLLISION = GAME OVER
        # -------------------------
        if (
            new_head[0] < 0 or new_head[0] >= self.grid_w or
            new_head[1] < 0 or new_head[1] >= self.grid_h
        ):
            self.game_over = True
            return

        # self collision
        if new_head in self.body:
            self.game_over = True
            return

        self.body.insert(0, new_head)

        # eat food
        if new_head == self.food:
            self.food = self.spawn_food()
        else:
            self.body.pop()

    # -------------------------
    # DRAW
    # -------------------------
    def draw(self, screen):
        screen.fill((0, 0, 0))

        # snake
        for b in self.body:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                (b[0]*self.cell, b[1]*self.cell, self.cell, self.cell)
            )

        # food
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (self.food[0]*self.cell, self.food[1]*self.cell, self.cell, self.cell)
        )

        # -------------------------
        # GAME OVER SCREEN
        # -------------------------
        if self.game_over:
            overlay = pygame.Surface((800, 600))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            title = self.font.render("GAME OVER", True, (255, 255, 255))
            screen.blit(title, title.get_rect(center=(400, 250)))

            hint = self.small.render("Press R to Restart or ESC for Menu", True, (200, 200, 200))
            screen.blit(hint, hint.get_rect(center=(400, 330)))