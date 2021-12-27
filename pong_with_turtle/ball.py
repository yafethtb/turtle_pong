from turtle import Turtle

class Ball(Turtle):
    '''Ball Class with methods to control how it moves'''
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')        
        self.speed('fastest')      
        self.goto(0, -20)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        '''Ball moves to new (x, y) position'''
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bounce(self):             
        '''y coordinate of ball is reversed my negative number of the incoming position'''
        self.y_move *= -1
    
    def collide(self):
        '''x coordinate of ball is reversed my negative number of the incoming position'''
        self.x_move *= -1
        