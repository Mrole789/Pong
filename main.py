from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#creating centre half-line
for x in range(18):
    halfline = Turtle()
    halfline.shape('square')
    halfline.shapesize(0.8,0.2,0.5)
    halfline.color('white')
    halfline.penup()
    halfline.goto(0,280-(x*30))

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

game_on = True
while game_on:
    screen.update()
        
    all_parts = [paddle.paddle_seg,paddle.paddle_seg2] #all paddle square parts
    ball.move(all_parts)
    time.sleep(ball.ball_speed)

    if ball.pos()[0] <= -400:
        user = 1
        scoreboard.increase_score(user)
        ball.refresh()
    elif ball.pos()[0] >= 400:
        user = 2
        scoreboard.increase_score(user)
        ball.refresh()
    
    screen.listen()
    screen.onkey(paddle.move_up, 'w')
    screen.onkey(paddle.move_down, 's')
    screen.onkey(paddle.move_up2, "Up")
    screen.onkey(paddle.move_down2, "Down")

screen.exitonclick()
