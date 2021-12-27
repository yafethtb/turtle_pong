from turtle import Turtle

class Plate(Turtle):

    def __init__(self, init_x, init_y):
        super().__init__()        
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(5, 0.5)
        self.goto(init_x, init_y)
        self.speed('fastest')
    
    def up(self):
        '''Control player plate moving up'''
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def down(self):
        '''Control plaer plate moving down'''
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)


    