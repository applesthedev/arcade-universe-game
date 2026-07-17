import pygame
import random

from ui.buttons import Button


class GuessGame:

    def __init__(self, save):

        self.save = save

        self.font = pygame.font.SysFont(None, 45)
        self.small_font = pygame.font.SysFont(None, 35)


        self.restart_button = Button(
            "Restart",
            680,
            220,
            150,
            60
        )


        self.leave_button = Button(
            "Leave",
            680,
            300,
            150,
            60
        )


        self.reset()



    def reset(self):

        self.number = random.randint(1,100)

        self.guess = ""

        self.message = "Guess a number 1-100"

        self.guess_count = 0

        self.finished = False



    def save_result(self):

        if self.guess_count > 0:

            if self.guess_count < self.save["guess_best"]:

                self.save["guess_best"] = self.guess_count




    def handle_event(self,event):


        if event.type == pygame.KEYDOWN:


            if not self.finished:


                if event.key == pygame.K_BACKSPACE:

                    self.guess = self.guess[:-1]



                elif event.unicode.isdigit():


                    if len(self.guess) < 3:

                        self.guess += event.unicode




                elif event.key == pygame.K_RETURN:



                    if self.guess:


                        value = int(self.guess)

                        self.guess_count += 1



                        if value < self.number:


                            self.message = "Too low!"



                        elif value > self.number:


                            self.message = "Too high!"



                        else:


                            self.message = "You win!"

                            self.finished = True

                            self.save_result()



                        self.guess = ""






        if event.type == pygame.MOUSEBUTTONDOWN:



            if self.restart_button.clicked(event.pos):

                self.reset()




            if self.leave_button.clicked(event.pos):

                self.save_result()

                return "menu"




        return None





    def draw(self,screen):


        pygame.draw.rect(
            screen,
            (30,30,40),
            (600,0,350,600)
        )



        title = self.font.render(
            "Guess Game",
            True,
            (255,255,255)
        )


        screen.blit(
            title,
            (50,80)
        )




        number = self.font.render(
            "Your guess: " + self.guess,
            True,
            (255,255,255)
        )


        screen.blit(
            number,
            (50,180)
        )




        message = self.small_font.render(
            self.message,
            True,
            (255,255,0)
        )


        screen.blit(
            message,
            (50,260)
        )




        count = self.small_font.render(
            "Attempts: " + str(self.guess_count),
            True,
            (255,255,255)
        )


        screen.blit(
            count,
            (50,320)
        )




        best = self.small_font.render(
            "Best: " + str(self.save["guess_best"]),
            True,
            (0,255,0)
        )


        screen.blit(
            best,
            (50,380)
        )




        self.restart_button.draw(screen)

        self.leave_button.draw(screen)