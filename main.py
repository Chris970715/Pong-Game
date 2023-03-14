from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreBoard import ScoreBoard

# Screen set up
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # turning off animation not to show users the setting process

game_is_on = True

#Bar Creation
paddle = Paddle((350, 0)) # Tuple (x_postion , y_position)
another_paddle = Paddle((-350,0))
ball = Ball()


#Bar Game Settings
scoreBoard = ScoreBoard()
screen.listen()
screen.onkey(paddle.up,"Up")
screen.onkey(paddle.down,"Down")

screen.onkey(another_paddle.up,"w")
screen.onkey(another_paddle.down,"s")

#Game
while(game_is_on):
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()



    if ((ball.ycor() > 280) or (ball.ycor() < -280)):
        ball.bounce_y()

    # Detect collision with paddle
    if ((ball.distance(paddle) < 50 and ball.xcor() > 320) or (ball.distance(another_paddle) < 50 and ball.xcor() < -320)):
        ball.bounce_x()

    if(ball.xcor() > 400):
        ball.reset()
        scoreBoard.l_point()
    if(ball.xcor() < -400):
        ball.reset()
        scoreBoard.r_point()


#exit
screen.exitonclick()