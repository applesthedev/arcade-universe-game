import pygame


class Popup:

    def __init__(self):

        self.font = pygame.font.SysFont(None, 40)
        self.small_font = pygame.font.SysFont(None, 30)

        self.message = ""
        self.timer = 0


    def show(self, message):

        self.message = message
        self.timer = 180


    def update(self):

        if self.timer > 0:
            self.timer -= 1


    def draw(self, screen):

        if self.timer <= 0:
            return


        box = pygame.Rect(
            200,
            220,
            550,
            180
        )


        pygame.draw.rect(
            screen,
            (40,40,50),
            box
        )


        pygame.draw.rect(
            screen,
            (255,255,0),
            box,
            3
        )


        title = self.font.render(
            "Coming Soon!",
            True,
            (255,255,255)
        )


        screen.blit(
            title,
            (360,250)
        )


        text = self.small_font.render(
            self.message,
            True,
            (255,255,0)
        )


        screen.blit(
            text,
            (270,320)
        )