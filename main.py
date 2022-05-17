# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:22:20 2018

@author: zou
"""
from tkinter import *
from tkinter import Button

import pygame
import time
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE
from pygame.locals import QUIT
from PIL import Image
from PIL import ImageTk

from game import Game

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

green = pygame.Color(0, 200, 0)
bright_green = pygame.Color(0, 255, 0)
red = pygame.Color(200, 0, 0)
bright_red = pygame.Color(255, 0, 0)
blue = pygame.Color(32, 178, 170)
bright_blue = pygame.Color(32, 200, 200)
yellow = pygame.Color(255, 205, 0)
bright_yellow = pygame.Color(255, 255, 0)
pygame.init()
fpsClock = pygame.time.Clock()
from game import Settings

settings = Settings()
screen = pygame.display.set_mode((settings.width * 15, settings.height * 15))
pygame.display.set_caption('Gluttonous')

crash_sound = pygame.mixer.Sound('./sound/crash.wav')
class CanvasButton:#home button class
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root=root

        self.button = Button(canvas, text='Home',
                                command=self.buttonclicked)
        self.id = canvas.create_window(100, 300, width=100, height=50,
                                       window=self.button)
    def buttonclicked(self):
        self.root.destroy()

class ExitButton:#exit button class
    def __init__(self, canvas):
        self.canvas = canvas
        self.button = Button(canvas, text='Exit',
                                command=self.buttonclicked)
        self.id = canvas.create_window(400, 300, width=100, height=50,
                                       window=self.button)
    def buttonclicked(self):
        exit()
def text_objects(text, font, color=black):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_display(text, x, y, color=black):
    large_text = pygame.font.SysFont('comicsansms', 50)
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = (x, y)
    screen.blit(text_surf, text_rect)
    pygame.display.update()


def button(msg, x, y, w, h, inactive_color, active_color, action=None, parameter=None, answer=None):  #####
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if answer != None:
        global wrap
        wrap = answer

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            if parameter != None:
                action(parameter)
            else:
                action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))

    smallText = pygame.font.SysFont('comicsansms', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = (x + (w / 2), y + (h / 2))
    screen.blit(TextSurf, TextRect)


def quitgame():
    pygame.quit()
    quit()



def crash():
    pygame.mixer.Sound.play(crash_sound)
    message_display('CRASHED!', game.settings.width / 2 * 15, game.settings.height / 3 * 15, bright_red)
    i = 0
    while i < 999999:
        i = i + 1
    global root
    root = Tk()
    root.resizable(width=False, height=False)
    root.wm_attributes("-topmost", 1)
    root.title('HAHA NOOB')

    imgpath = 'images/you_lose.png'#for some ungodly reason it only works with pngs and not jpgs
    img = Image.open(imgpath)
    photo = ImageTk.PhotoImage(img)


    canvas = Canvas(root, bd=0, highlightthickness=0)
    canvas.pack()
    canvas.create_image(250,175, image=photo)
    canvas.config(width=500, height=350)

    CanvasButton(canvas,root)
    ExitButton(canvas)# create a clickable button on the canvas


    root.mainloop()





# crash message
display_width = 900
display_height = 550
def initial_interface():  # homepage
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        SnakeImg = pygame.image.load('images/background.png')
        SnakeImg = pygame.transform.scale(SnakeImg, (display_width, display_height))


        x = 0
        y = 0
        gameDisplay = pygame.display.set_mode((display_width, display_height))
        gameDisplay.blit(SnakeImg, (x, y))
        # message_display('Gluttonous', game.settings.width / 2 * 15, game.settings.height / 4 * 15)

        button('Go!', 50, 480, 160, 40, green, bright_green, game_loop, 'human')
        button('Quit', 320, 480, 160, 40, red, bright_red, quitgame)
        button('No wrap', 80, 420, 80, 40, green, bright_green, game_loop, 'human', False)
        button('Wrap', 350, 420, 80, 40, green, bright_green, game_loop, 'human', True)


        pygame.display.update()
        pygame.time.Clock().tick(15)


def game_loop(player, fps=10):
    from game import Game  ######
    global game
    game = Game(wrap)
    game.restart_game()
    rect_len = game.settings.rect_len
    snake = game.snake

    while not game.game_end():
        pygame.event.pump()

        move = human_move(snake)
        fps = 5

        game.do_move(move)

        screen.fill(black)

        game.snake.blit(rect_len, screen)
        game.strawberry.blit(screen)
        game.blit_score(white, screen)

        pygame.display.flip()

        fpsClock.tick(fps)

    crash()


def human_move(snake):
    direction = snake.facing

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                direction = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                direction = 'left'
            if event.key == K_UP or event.key == ord('w'):
                direction = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                direction = 'down'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    move = game.direction_to_int(direction)
    return move


if __name__ == "__main__":
    initial_interface()

