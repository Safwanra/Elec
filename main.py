
from tkinter import *
from tkinter import Button
from tkinter import ttk
import tkinter as tk

from pickle import TRUE

import pygame
import time
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE
from pygame.locals import QUIT
from PIL import Image
from PIL import ImageTk

from os import path


from game import Game
from game import Settings


speed = "10"
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

green = pygame.Color(0, 200, 0)
bright_green = pygame.Color(0, 255, 0)
red = pygame.Color(200, 0, 0)
bright_red = pygame.Color(255, 0, 0)
grey = pygame.Color(80, 80, 80)
blue = pygame.Color(32, 178, 170)
bright_blue = pygame.Color(32, 200, 200)
yellow = pygame.Color(255, 205, 0)
bright_yellow = pygame.Color(255, 255, 0)
# setting the color
pygame.init()
fpsClock = pygame.time.Clock()
ranking_score = "ranking_score.txt"
ranking_name = "ranking_name.txt"
settings = Settings()
screen = pygame.display.set_mode((settings.width * 15, settings.height * 15))
pygame.display.set_caption('Gluttonous')

crash_sound = pygame.mixer.Sound('./sound/sound_end.wav') #assigning the crash sound
class HomeButton:#home button class
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root=root

        self.button = Button(canvas, text='Home',
                                command=self.buttonclicked)
        self.id = canvas.create_window(100, 300, width=100, height=50,
                                       window=self.button)
    def buttonclicked(self):
        self.root.destroy()

class Exit1Button:#exit button class
    def __init__(self, canvas):
        self.canvas = canvas
        self.button = Button(canvas, text='Exit',
                                command=self.buttonclicked)
        self.id = canvas.create_window(400, 300, width=100, height=50,
                                       window=self.button)
    def buttonclicked(self):
        exit()
class Exit2Button:#exit button class
    def __init__(self, canvas):
        self.canvas = canvas
        self.button = Button(canvas, text='Exit',
                                command=self.buttonclicked)
        self.id = canvas.create_window(445, 320, width=100, height=50,
                                       window=self.button)
    def buttonclicked(self):
        exit()
class SubmitButton:#submit button class
    def __init__(self, canvas):
        self.canvas = canvas
        self.button = Button(canvas, text='Submit',
                                command=self.buttonclicked)
        self.id = canvas.create_window(55, 320, width=100, height=50,
                                       window=self.button)
    def buttonclicked(self):    # text objects function ->it can render a given text into an image.
        click()
def text_objects(text, font, color=black):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_display(text, x, y, color=black): #create a fonts, with comicsansms at a size of 50
    large_text = pygame.font.SysFont('comicsansms', 50)
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = (x, y)
    screen.blit(text_surf, text_rect)
    pygame.display.update()


def button(msg, x, y, w, h, inactive_color, active_color, action=None, parameter=None, answer=None):  #ask dang and dohyun
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
    screen.blit(TextSurf, TextRect)#button function -> used to set the appearance of button on the homepage, and also set the font and the size on the button.
def click():#this is where the user select the speed
    user_text = T.get()
    if user_text.isdigit() and int(user_text) <= 19 and int(user_text) >= 10:
        global speed_button
        speed_button = user_text
        global speed
        speed = user_text
        root.destroy()

def tk_name():#Your name button class
    root = Tk()
    root.geometry("300x200")
    root.title("Your name")

    global user_name
    user_name = ""

    def click():#this is where the user types in their name
        user_text = T.get()
        # myLabel = Label(root, text=user_text)
        # myLabel.pack()

        global button_name
        button_name = user_text
        global user_name
        user_name = user_text

        root.destroy()

    one = Label(root, text="Enter your name")
    one.config(font=("Courier", 17))

    T = Entry(root, width=10, borderwidth=4, justify='center')
    b1 = Button(root, text="Submit", command=click)

    one.pack()
    T.pack()
    b1.pack()

    # FURTHER MODIFIED; for ranking board
    # First prepare all lists
    f_score = open(ranking_score, 'r')  # txt file of ranking_score
    player_scores_temp = f_score.readline()
    player_scores_temp = player_scores_temp.strip('][').split(", ")  # Convert string to list
    if player_scores_temp == ['']:  # If intial list was empty, [''] is generated
        player_scores_temp = []
    # This list currently contains strings. Need to convert them to integer
    t = 0
    while t < len(player_scores_temp):
        player_scores_temp[t] = int(player_scores_temp[t])
        t += 1

    f_name = open(ranking_name, 'r')  # txt file of ranking_name
    player_names_temp = f_name.readline()
    player_names_temp = player_names_temp.strip('][').split(", ")  # Convert string to list
    if player_names_temp == ['']:  # If intial list was empty, [''] is generated
        player_names_temp = []

    x = 1  # now in REVERSE ORDER
    player_names = []
    player_scores = []
    while -x >= -len(player_scores_temp):
        player_names.append(player_names_temp[-x])
        player_scores.append(player_scores_temp[-x])
        x += 1

    ranking_order = []
    j = 0
    while j < len(player_scores):
        ranking_order.append(j + 1)
        j += 1

    # THEN table
    game_frame = Frame(root)
    game_frame.pack()

    # scrollbar
    game_scroll = Scrollbar(game_frame)
    game_scroll.pack(side=RIGHT, fill=Y)
    my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)
    my_game.pack()

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    # define our column
    my_game['columns'] = ('player_Ranking', 'player_Name', 'player_Score')

    # format our column
    my_game.column("#0", width=0, stretch=NO)
    my_game.column("player_Ranking", anchor=CENTER, width=80)
    my_game.column("player_Name", anchor=CENTER, width=80)
    my_game.column("player_Score", anchor=CENTER, width=80)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("player_Ranking", text="Ranking", anchor=CENTER)
    my_game.heading("player_Name", text="Name", anchor=CENTER)
    my_game.heading("player_Score", text="Score", anchor=CENTER)

    i = 0
    while i < len(player_scores):
        my_game.insert(parent='', index='end',  # iid=0, text='',
                       values=(ranking_order[i], player_names[i], player_scores[i]))
        i += 1

    my_game.pack()

    root.mainloop()

def tk_speed():#selecting speed
    global root
    root = Tk()
    #root.geometry("350x170")
    root.resizable(width=False, height=False)
    root.wm_attributes("-topmost", 1)
    root.title("Speed")
    imgpath = 'images/i-am-speed.png'  
    img = Image.open(imgpath)
    photo = ImageTk.PhotoImage(img)




    one = Label(root, text="Enter speed \n between 10 and 19")
    one.config(font=("Courier", 17))
    global T
    T = Entry(root, width=10, borderwidth=4, justify='center')

    #b1 = Button(root, text="Submit", command=click)
    #b2 = Button(root, text="Exit", command=root.destroy)
    canvas = Canvas(root, bd=0, highlightthickness=0)
    canvas.pack()
    canvas.create_image(250, 175, image=photo)
    canvas.config(width=500, height=350)

    SubmitButton(canvas)
    Exit2Button(canvas)

    one.pack()
    T.pack()
    #b1.pack()
    #b2.pack()
    root.mainloop()


def quitgame():
    pygame.quit()
    quit()


def crash(score):#the pop up window the game ends 
    pygame.mixer.Sound.play(crash_sound)
    i = 0
    while i < 999999:
        i = i + 1
    global root
    root = Tk()
    root.resizable(width=False, height=False)
    root.wm_attributes("-topmost", 1)
    root.title('HAHA NOOB')

    imgpath = 'images/you_lose.png'
    img = Image.open(imgpath)
    photo = ImageTk.PhotoImage(img)


    canvas = Canvas(root, bd=0, highlightthickness=0)
    canvas.pack()
    canvas.create_image(250,175, image=photo)
    canvas.config(width=500, height=350)

    HomeButton(canvas,root)
    Exit1Button(canvas)# create a clickable button on the canvas



    global user_name
    if user_name == "":  # IF user did not entered their name;
        user_name = "Outis"  # temporary name

    message_display('crashed', game.settings.width / 2 * 15, game.settings.height / 3 * 15, white)
    message_display(f'Score: {score}', game.settings.width / 2 * 15, game.settings.height / 3 * 15 + 60, white) \
 \
        # MODIFIED
    # txt file of ranking_score, add score
    f_score = open(ranking_score, 'r')
    player_scores = f_score.readline()
    player_scores = player_scores.strip('][').split(", ")  # Convert string to list
    if player_scores == ['']:  # If intial list was empty, [''] is generated
        player_scores = []
    # This list currently contains strings. Need to convert them to integer
    t = 0
    while t < len(player_scores):
        player_scores[t] = int(player_scores[t])
        t += 1
    player_scores.append(score)  # Add new score
    f_score.close()

    # txt file of ranking_name, add user name
    f_name = open(ranking_name, 'r')
    player_names = f_name.readline()
    player_names = player_names.strip('][').split(", ")  # Convert string to list
    if player_names == ['']:  # If intial list was empty, [''] is generated
        player_names = []
    player_names.append(user_name)
    f_name.close()

    # If correct, length of both lists should be equal
    length = len(player_scores)  # Add new user name

    # BUBBLE SORT; in ascending order
    for i in range(length):
        for j in range(0, length - i - 1):
            if player_scores[j] > player_scores[j + 1]:
                temp = player_scores[j]
                player_scores[j] = player_scores[j + 1]
                player_scores[j + 1] = temp
                # -----
                temp = player_names[j]
                player_names[j] = player_names[j + 1]
                player_names[j + 1] = temp

    while length > 10:  # Limit the length of array to 10
        # del player_scores[length-1]    For array of descending order
        # del player_names[length-1]     For array of descending order
        del player_scores[0]
        del player_names[0]
        length -= 1

    f = open(ranking_score, 'w')
    f.write(str(player_scores))
    f.close()
    f = open(ranking_name, 'w')
    f.write(str(player_names).replace("'", ""))  # For player_names; remove unwanter character '
    f.close()
    root.mainloop()




# crash message
display_width = 900
display_height = 550
def initial_interface():  # homepage
    global speed_button
    speed_button = "Speed"
    intro = True
    global user_name
    user_name = ""
    global button_name
    button_name = "Name"
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

        button('Quit', 320, 480, 80, 40, red, bright_red, quitgame)
        button(speed_button, 80, 480, 80, 40, yellow, bright_yellow, tk_speed)
        button(button_name, 200, 480, 80, 40, yellow, bright_yellow, tk_name)
        button('No wrap', 80, 420, 80, 40, green, bright_green, game_loop, 'human', False)
        button('Wrap', 320, 420, 80, 40, green, bright_green, game_loop, 'human', True)


        pygame.display.update()
        pygame.time.Clock().tick(15)


def game_loop(player, fps=10):
    # Below 2 lines are essential to make the snake initially move towards certain direction; objects are defined in each loop, and previous snake direction data is reset
    global game
    game = Game(wrap, speed)
    snake = game.snake
    rect_len = game.settings.rect_len

    game.restart_game()

    while not game.game_end():

        pygame.event.pump()

        move = human_move(
            snake)  # snake object is added inside brackets. To re-define objects in each loop, need to call the objects every time. Changed similary for 'def human_move' line
        fps = int(speed)

        # MODIFIED ORIGINAL CODE
        temp = game.do_move(move)
        if temp[1] != False:  # for testing
            print(f"{temp[1]} and {type(temp[1])}")

        screen.fill(black)

        game.snake.blit(rect_len, screen)
        game.strawberry.blit(screen)
        game.blit_score(white, screen)

        pygame.display.flip()

        fpsClock.tick(fps)

    # MODIFIED to take one variable
    crash(temp[1])


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
