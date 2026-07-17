import pygame
import random

from ui.buttons import Button
from core.save_system import save_game


class Snake:

    def __init__(self, save):

        self.save = save

        self.block = 25

        self.game_width = 600
        self.game_height = 600

        self.font = pygame.font.SysFont(None, 45)


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


        self.easy_button = Button(
            "Easy",
            620,
            380,
            100,
            50
        )


        self.hard_button = Button(
            "Hard",
            740,
            380,
            100,
            50
        )


        self.mode = "Easy"

        self.timer = 0
        self.speed = 8

        self.reset()



    def reset(self):

        self.snake = [
            [100,100],
            [75,100],
            [50,100]
        ]

        self.direction = "RIGHT"

        self.food = self.spawn_food()

        self.score = 0

        self.game_over = False



    def spawn_food(self):

        return [
            random.randint(0,23) * self.block,
            random.randint(0,19) * self.block
        ]



    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and self.direction != "DOWN":
                self.direction = "UP"

            elif event.key == pygame.K_DOWN and self.direction != "UP":
                self.direction = "DOWN"

            elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                self.direction = "LEFT"

            elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                self.direction = "RIGHT"



        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.restart_button.clicked(event.pos):
                self.reset()


            if self.leave_button.clicked(event.pos):

                # save before leaving
                self.save_score()

                return "menu"



            if self.easy_button.clicked(event.pos):
                self.mode = "Easy"


            if self.hard_button.clicked(event.pos):
                self.mode = "Hard"



        return None



    def save_score(self):

        if self.score > self.save["snake_highscore"]:

            self.save["snake_highscore"] = self.score

            save_game(self.save)



    def update(self):

        if self.game_over:

            self.save_score()

            return



        self.timer += 1


        if self.timer < self.speed:

            return


        self.timer = 0


        head = self.snake[0].copy()



        if self.direction == "UP":
            head[1] -= self.block

        elif self.direction == "DOWN":
            head[1] += self.block

        elif self.direction == "LEFT":
            head[0] -= self.block

        elif self.direction == "RIGHT":
            head[0] += self.block



        if self.mode == "Easy":


            if head[0] < 0:
                head[0] = self.game_width - self.block

            if head[0] >= self.game_width:
                head[0] = 0

            if head[1] < 0:
                head[1] = self.game_height - self.block

            if head[1] >= self.game_height:
                head[1] = 0



        else:


            if (
                head[0] < 0 or
                head[0] >= self.game_width or
                head[1] < 0 or
                head[1] >= self.game_height
            ):

                self.game_over = True



        self.snake.insert(0, head)



        if head == self.food:

            self.score += 1

            self.food = self.spawn_food()


        else:

            self.snake.pop()



        if head in self.snake[1:]:

            self.game_over = True



    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (30,30,40),
            (600,0,350,600)
        )


        pygame.draw.rect(
            screen,
            (150,150,150),
            (
                0,
                0,
                self.game_width,
                self.game_height
            ),
            4
        )


        for part in self.snake:

            pygame.draw.rect(
                screen,
                (0,200,0),
                (
                    part[0],
                    part[1],
                    self.block,
                    self.block
                )
            )


        pygame.draw.rect(
            screen,
            (255,0,0),
            (
                self.food[0],
                self.food[1],
                self.block,
                self.block
            )
        )


        score = self.font.render(
            "Score: " + str(self.score),
            True,
            (255,255,255)
        )

        screen.blit(score,(680,80))


        mode = self.font.render(
            self.mode,
            True,
            (255,255,0)
        )

        screen.blit(mode,(680,140))


        self.restart_button.draw(screen)

        self.leave_button.draw(screen)

        self.easy_button.draw(screen)

        self.hard_button.draw(screen)



        if self.game_over:

            text = self.font.render(
                "Game Over",
                True,
                (255,255,0)
            )

            screen.blit(text,(680,180))