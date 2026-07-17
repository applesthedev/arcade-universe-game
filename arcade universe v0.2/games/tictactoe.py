import pygame

from ui.buttons import Button


class TicTacToe:

    def __init__(self, save):

        self.save = save

        self.font = pygame.font.SysFont(None, 70)
        self.small_font = pygame.font.SysFont(None, 40)


        self.buttons = [
            Button("Restart", 520, 180, 250, 60),
            Button("Leave", 520, 260, 250, 60),
            Button("AI", 520, 340, 250, 60)
        ]


        self.reset()



    def reset(self):

        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        self.turn = "X"

        self.finished = False

        self.winner = ""



    def save_result(self):

        if self.winner == "X":

            if "tictactoe_wins" not in self.save:

                self.save["tictactoe_wins"] = 0


            self.save["tictactoe_wins"] += 1





    def handle_event(self, event):


        if event.type == pygame.MOUSEBUTTONDOWN:



            for button in self.buttons:



                if button.clicked(event.pos):



                    if button.text == "Restart":

                        self.reset()



                    elif button.text == "Leave":

                        return "menu"



                    elif button.text == "AI":

                        print("AI coming in v0.3!")





            if not self.finished:



                x, y = event.pos


                col = x // 150

                row = y // 150



                if row < 3 and col < 3:



                    if self.board[row][col] == "":



                        self.board[row][col] = self.turn




                        if self.check_win():



                            self.finished = True

                            self.winner = self.turn

                            self.save_result()



                        else:



                            if self.turn == "X":

                                self.turn = "O"

                            else:

                                self.turn = "X"




        return None






    def check_win(self):



        for row in self.board:



            if row[0] != "" and row[0] == row[1] == row[2]:

                return True





        for col in range(3):



            if (
                self.board[0][col] != "" and
                self.board[0][col] == self.board[1][col] ==
                self.board[2][col]
            ):

                return True





        if (
            self.board[0][0] != "" and
            self.board[0][0] == self.board[1][1] ==
            self.board[2][2]
        ):

            return True





        if (
            self.board[0][2] != "" and
            self.board[0][2] == self.board[1][1] ==
            self.board[2][0]
        ):

            return True





        return False





    def draw(self, screen):


        for y in range(3):

            for x in range(3):


                rect = pygame.Rect(
                    x * 150,
                    y * 150,
                    150,
                    150
                )


                pygame.draw.rect(
                    screen,
                    (100,100,100),
                    rect,
                    3
                )



                if self.board[y][x]:


                    text = self.font.render(
                        self.board[y][x],
                        True,
                        (255,255,255)
                    )


                    screen.blit(
                        text,
                        text.get_rect(center=rect.center)
                    )




        for button in self.buttons:

            button.draw(screen)





        if self.finished:


            text = self.small_font.render(
                self.winner + " wins!",
                True,
                (255,255,0)
            )


            screen.blit(
                text,
                (520,100)
            )