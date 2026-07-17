import pygame

from ui.buttons import Button


class Menu:

    def __init__(self, popup):

        self.popup = popup

        self.title_font = pygame.font.SysFont(None, 60)
        self.footer_font = pygame.font.SysFont(None, 24)

        self.fade = 0


        self.buttons = [

            Button("Snake", 300, 170, 300, 60),

            Button("Guess Game", 300, 240, 300, 60),

            Button("Tic-Tac-Toe", 300, 310, 300, 60),

            Button("Breakout", 300, 380, 300, 60),

            Button("Flappy Bird", 300, 450, 300, 60)

        ]



    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:


            for button in self.buttons:


                if button.clicked(event.pos):


                    if button.text == "Snake":

                        return "snake"



                    elif button.text == "Guess Game":

                        return "guess"



                    elif button.text == "Tic-Tac-Toe":

                        return "tictactoe"



                    elif button.text == "Breakout":

                        self.popup.show(
                            "Breakout - Done in v0.3"
                        )



                    elif button.text == "Flappy Bird":

                        self.popup.show(
                            "Flappy Bird - Done in v1.0"
                        )



        return None





    def draw(self, screen):


        if self.fade < 255:

            self.fade += 4


        alpha = min(self.fade,255)




        title = self.title_font.render(

            "Arcade Universe",

            True,

            (255,255,255)

        )


        title.set_alpha(alpha)



        screen.blit(

            title,

            (240,70)

        )





        info = self.footer_font.render(

            "v0.2 - Foundation Update",

            True,

            (180,180,180)

        )


        info.set_alpha(alpha)



        screen.blit(

            info,

            (350,125)

        )





        for button in self.buttons:

            button.draw(screen)





        footer = self.footer_font.render(

            "Made with Pygame",

            True,

            (140,140,140)

        )


        screen.blit(

            footer,

            (15,570)

        )





        version = self.footer_font.render(

            "v0.2",

            True,

            (140,140,140)

        )


        screen.blit(

            version,

            (900,570)

        )