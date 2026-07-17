import pygame

from ui.menu import Menu
from ui.popup import Popup

from games.snake import Snake
from games.guess import GuessGame
from games.tictactoe import TicTacToe

from core.save_system import load_save, save_game



pygame.init()



WIDTH = 950
HEIGHT = 600



screen = pygame.display.set_mode(
    (WIDTH,HEIGHT)
)


pygame.display.set_caption(
    "Arcade Universe"
)



clock = pygame.time.Clock()



save = load_save()



popup = Popup()


menu = Menu(popup)

snake = Snake(save)

guess = GuessGame(save)

tictactoe = TicTacToe(save)



state = "menu"



running = True



while running:


    for event in pygame.event.get():


        if event.type == pygame.QUIT:

            running = False



        if state == "menu":


            result = menu.handle_event(event)


            if result == "snake":

                state = "snake"



            elif result == "guess":

                state = "guess"



            elif result == "tictactoe":

                state = "tictactoe"




        elif state == "snake":


            result = snake.handle_event(event)


            if result == "menu":

                save_game(save)

                state = "menu"




        elif state == "guess":


            result = guess.handle_event(event)


            if result == "menu":

                save_game(save)

                state = "menu"




        elif state == "tictactoe":


            result = tictactoe.handle_event(event)


            if result == "menu":

                save_game(save)

                state = "menu"




    popup.update()



    screen.fill(
        (20,20,30)
    )



    if state == "menu":

        menu.draw(screen)



    elif state == "snake":

        snake.update()

        snake.draw(screen)



    elif state == "guess":

        guess.draw(screen)



    elif state == "tictactoe":

        tictactoe.draw(screen)




    popup.draw(screen)



    pygame.display.flip()


    clock.tick(60)




save_game(save)


pygame.quit()