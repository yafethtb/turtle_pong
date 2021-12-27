from turtle import Turtle

class Scoreboard(Turtle):
    '''Score object. Show how much player hit and bounce the ball or send 'Game Over' message if miss it'''
    def __init__(self, name, init_x, init_y):
        super().__init__()
        self.name = name
        self.score = 0
        self.penup()
        self.goto(init_x, init_y)
        self.color('white')
        self.hideturtle()
        self.write(f'Score: {self.score}', align = 'center', font = ('courier', 12, 'bold'))

    def game_over(self):
        '''Show 'GAME OVER' message when player cannot bounce the ball back'''
        self.goto(0, 0)
        self.write(f"{self.name}, GAME OVER!", align = 'center', font = ('courier', 30, 'bold'))

    def add_score(self):
        '''Adding score to player each time player can bounce the ball back'''
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', align = 'center', font = ('courier', 12, 'bold'))


class Lines(Turtle):
    ''' Marking line to divide between play zone and score zone'''
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-270, 270)
        self.color('white')
        self.pendown()
        self.goto(270, 270)
        self.hideturtle()


class Marker(Turtle):
    '''Marking line to divide the screen'''
    def __init__ (self):
        super().__init__()
        self.penup()
        self.goto(0, 260)
        self.pendown()
        self.pensize(3)
        self.color('white')        
        self.goto(0, -280)
        self.hideturtle()
        

