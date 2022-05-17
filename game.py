import pygame, random
import numpy as np

# Initialising the calss Settings -> used to set size of game screen.
class Settings:
    def __init__(self):
        self.width = 42
        self.height = 25
        self.rect_len = 22


 UIbranch
# from main import wrap # Initialising the calss Settings -> used to set direction of snake's head and tail.
class Snake:
    def __init__(self, wrap):  #####
=======
#from main import wrap
class Snake:
    def __init__(self, wrap): #####
 main
        self.settings = Settings()
        self.image_up = pygame.image.load('images/head_up.bmp')
        self.image_down = pygame.image.load('images/head_down.bmp')
        self.image_left = pygame.image.load('images/head_left.bmp')
        self.image_right = pygame.image.load('images/head_right.bmp')

        self.tail_up = pygame.image.load('images/tail_up.bmp')
        self.tail_down = pygame.image.load('images/tail_down.bmp')
        self.tail_left = pygame.image.load('images/tail_left.bmp')
        self.tail_right = pygame.image.load('images/tail_right.bmp')

        self.image_body = pygame.image.load('images/body.bmp')

        self.facing = "right"
        self.wrap = wrap
        self.initialize()
# Initialising the function -> used to set the snake's positon and the game score when start the game.
    def initialize(self):
        self.position = [6, 6]
        self.segments = [[6 - i, 6] for i in range(3)]
        self.score = 0
 # Blit_body function -> used to set the snake's body in the screen during the play game.
    def blit_body(self, x, y, screen):
        screen.blit(self.image_body, (x, y))
# Blit_head function -> used to set the snake's head how to move during the play game.
    def blit_head(self, x, y, screen):
        if self.facing == "up":
            screen.blit(self.image_up, (x, y))
        elif self.facing == "down":
            screen.blit(self.image_down, (x, y))
        elif self.facing == "left":
            screen.blit(self.image_left, (x, y))
        else:
            screen.blit(self.image_right, (x, y))
# Blit_tail function -> used to set the snake's tail how to move during the play game.
    def blit_tail(self, x, y, screen):
        tail_direction = [self.segments[-2][i] - self.segments[-1][i] for i in range(2)]

        if tail_direction == [0, -1]:
            screen.blit(self.tail_up, (x, y))
        elif tail_direction == [0, 1]:
            screen.blit(self.tail_down, (x, y))
        elif tail_direction == [-1, 0]:
            screen.blit(self.tail_left, (x, y))
        else:
            screen.blit(self.tail_right, (x, y))
# Blit funcintion -> used to set the snake's move range in the screen.
    def blit(self, rect_len, screen):
        self.blit_head(self.segments[0][0] * rect_len, self.segments[0][1] * rect_len, screen)
        for position in self.segments[1:-1]:
            self.blit_body(position[0] * rect_len, position[1] * rect_len, screen)
        self.blit_tail(self.segments[-1][0] * rect_len, self.segments[-1][1] * rect_len, screen)
# Update function -> used to set the  when snake's move the position will change.
    def update(self):
 UIbranch
        if self.facing == 'right':  ######

        if self.facing == 'right':######
 main
            self.position[0] += 1
        if self.facing == 'left':
            self.position[0] -= 1
        if self.facing == 'up':
            self.position[1] -= 1
        if self.facing == 'down':
            self.position[1] += 1
        if self.wrap == True:
 UIbranch
            if self.position[0] >= self.settings.width:
                self.position[0] = 0
            if self.position[0] < 0:
                self.position[0] = self.settings.width - 1
            if self.position[1] >= self.settings.height:
                self.position[1] = 0
            if self.position[1] < 0:
                self.position[1] = self.settings.height - 1
=======
            if self.position[0] >= self.settings.width: 
                self.position [0] = 0
            if self.position[0] < 0:
                self.position [0] = self.settings.width-1
            if self.position[1] >= self.settings.height:
                self.position[1] = 0
            if self.position[1] < 0:
                self.position[1] = self.settings.height-1
 main
        self.segments.insert(0, list(self.position))

# Initialising the calss Settings -> used to Randomly generate strawberries on the screen.
class Strawberry():
    def __init__(self, settings):
        self.settings = settings

        self.style = str(random.randint(1, 8))
        self.image = pygame.image.load('images/food' + str(self.style) + '.bmp')
        self.initialize()

    def random_pos(self, snake):
        self.style = str(random.randint(1, 8))

        self.image = pygame.image.load('images/food' + str(self.style) + '.bmp')
        self.position[0] = random.randint(0, self.settings.width - 1)
        self.position[1] = random.randint(0, self.settings.height - 1)
=======
        self.image = pygame.image.load('images/food' + str(self.style) + '.bmp')                
        self.position[0] = random.randint(0, self.settings.width-1)
        self.position[1] = random.randint(0, self.settings.height-1)
 main
        self.position[0] = random.randint(9, 19)
        self.position[1] = random.randint(9, 19)
        if self.position in snake.segments:
            self.random_pos(snake)

    def blit(self, screen):
        screen.blit(self.image, [p * self.settings.rect_len for p in self.position])

    def initialize(self):
        self.position = [15, 10]

# Initialising the calss Settings -> used to set the  assign values for setting ,snake strawberry and move_dict.
class Game:
    """
    """


    def __init__(self, wrap):  ######
        self.settings = Settings()
        self.snake = Snake(wrap)
        self.strawberry = Strawberry(self.settings)
        self.move_dict = {0: 'up',
                          1: 'down',
                          2: 'left',
                          3: 'right'}
        self.wrap = wrap

    def __init__(self, wrap):######
        self.settings = Settings()
        self.snake = Snake(wrap)
        self.strawberry = Strawberry(self.settings)
        self.move_dict = {0 : 'up',
                          1 : 'down',
                          2 : 'left',
                          3 : 'right'}
        self.wrap = wrap


# When the game angin, assign values for snake  and strawberry angin.
 main
    def restart_game(self):
        self.snake.initialize()
        self.strawberry.initialize()

    def current_state(self):
        state = np.zeros((self.settings.width + 2, self.settings.height + 2, 2))
        expand = [[0, 1], [0, -1], [-1, 0], [1, 0], [0, 2], [0, -2], [-2, 0], [2, 0]]

        for position in self.snake.segments:
            state[position[1], position[0], 0] = 1

        state[:, :, 1] = -0.5

        state[self.strawberry.position[1], self.strawberry.position[0], 1] = 0.5
        for d in expand:
            state[self.strawberry.position[1] + d[0], self.strawberry.position[0] + d[1], 1] = 0.5
        return state

    def direction_to_int(self, direction):
        direction_dict = {value: key for key, value in self.move_dict.items()}
        return direction_dict[direction]
# Do_move function -> used to When I hit the direction key on the keyboard, the snake will move in the specified direction.
    def do_move(self, move):
        move_dict = self.move_dict

        change_direction = move_dict[move]

        if change_direction == 'right' and not self.snake.facing == 'left':
            self.snake.facing = change_direction
        if change_direction == 'left' and not self.snake.facing == 'right':
            self.snake.facing = change_direction
        if change_direction == 'up' and not self.snake.facing == 'down':
            self.snake.facing = change_direction
        if change_direction == 'down' and not self.snake.facing == 'up':
            self.snake.facing = change_direction

        self.snake.update()
        # Used to set the how to add the score.
        if self.snake.position == self.strawberry.position:
            self.strawberry.random_pos(self.snake)
            reward = 1
            self.snake.score += 1
        else:
            self.snake.segments.pop()
            reward = 0
        # Game_end function -> used to set when the sanke touch the edge of screen and the game end.
        if self.game_end():
            return -1

        return reward
 UIbranch

    def game_end(self):  #####

    
    def game_end(self):#####
 main
        end = False
        if (self.snake.position[0] >= self.settings.width or self.snake.position[0] < 0) and self.wrap == False:
            end = True
        if (self.snake.position[1] >= self.settings.height or self.snake.position[1] < 0) and self.wrap == False:
            end = True
        if self.snake.segments[0] in self.snake.segments[1:]:
            end = True

        return end
# Blit_score function -> used to set  when the game over the score will display in the screen.
    def blit_score(self, color, screen):
        font = pygame.font.SysFont(None, 25)
        text = font.render('Score: ' + str(self.snake.score), True, color)
        screen.blit(text, (0, 0))

