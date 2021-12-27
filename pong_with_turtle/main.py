from turtle import Screen
from plate import Plate
from ball import Ball
from  scoreboard import Scoreboard, Lines, Marker
import time

# Screen initializing
screen = Screen()
screen.setup(900, 600)
screen.bgcolor('black')
screen.title("Pong With Turtle Module")
screen.tracer(0)

# Objects initializing
plate = Plate(400, 0)
plate_02 = Plate(-400, 0)
ball = Ball()
score = Scoreboard("Me", 280, 280)
score_02 = Scoreboard("Other", -280, 280)
line = Lines()
marking = Marker()

# Game blocks
game_start = True
while game_start:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    
    # Plates control. Right plate with up and down keys, left plate with 'w' and 's' keys
    screen.onkeypress(plate.up, "Up")
    screen.onkeypress(plate.down, "Down")
    screen.onkeypress(plate_02.up, "w")
    screen.onkeypress(plate_02.down, "s")

    # Function to move ball
    ball.move()

    # Ball collision with upper and lower 'walls'
    if ball.ycor() < -250 or ball.ycor() > 250:
        ball.bounce()
    
    # Ball collision with player plate
    if ball.distance(plate) < 30 and ball.xcor() > 380:
        ball.collide()
        score.add_score()
    elif ball.xcor() > 400:
        marking.clear()
        score.game_over()
        game_start =  False
    
    # Ball collision with plate_02
    if ball.distance(plate_02) < 30 and ball.xcor() > - 390:
        ball.collide()
        score_02.add_score()
    elif ball.xcor() < -400:
        marking.clear()
        score_02.game_over()        
        game_start =  False    

screen.mainloop()