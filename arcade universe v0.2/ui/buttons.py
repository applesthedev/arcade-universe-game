import pygame


class Button:

    def __init__(self, text, x, y, width, height):

        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

        self.font = pygame.font.SysFont(None, 35)

        # Render text once
        self.text_surface = self.font.render(
            self.text,
            True,
            (255, 255, 255)
        )

        self.color = 70
        self.target_color = 70

        self.hover_speed = 0.20


    def draw(self, screen):

        mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse):
            self.target_color = 110
        else:
            self.target_color = 70

        self.color += (self.target_color - self.color) * self.hover_speed

        pygame.draw.rect(
            screen,
            (
                int(self.color),
                int(self.color),
                int(self.color + 20)
            ),
            self.rect,
            border_radius=20
        )

        text_rect = self.text_surface.get_rect(
            center=self.rect.center
        )

        screen.blit(
            self.text_surface,
            text_rect
        )


    def clicked(self, pos):
        return self.rect.collidepoint(pos)