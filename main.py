from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Setting the screen/canvas
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.tracer(0)

#Creating the players paddle
r_paddle = Paddle(initial_x=350, initial_y=0)
l_paddle = Paddle(initial_x=-350, initial_y=0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_south, 'Up')
screen.onkey(r_paddle.go_north, 'Down')

screen.onkey(l_paddle.go_south, 'w')
screen.onkey(l_paddle.go_north, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bouce_wall()

    #detect collision with right paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bouce_paddle()

    #detect collision with left paddles
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bouce_paddle()
    
    #detect if right player missed the ball
    if ball.xcor() > 390:
        ball.ball_reset()
        scoreboard.l_point()
    #detect if left player misse
    # d the ball
    if ball.xcor() < -390:
        ball.ball_reset()
        scoreboard.r_point()

screen.exitonclick()
