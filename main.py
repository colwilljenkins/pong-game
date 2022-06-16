from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scorebaord import Scoreboard

LEFT_PADDLE = (-350, 0)
RIGHT_PADDLE = (350, 0)

screen = Screen()
screen.bgcolor('black')
screen.title('PONG')
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle(LEFT_PADDLE)
r_paddle = Paddle(RIGHT_PADDLE)

ball = Ball()
scorebaord = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball_speed = 0.1
while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    # hits top or bottom wall
    if ball.ycor() > 282 or ball.ycor() < -282:
        # bounce
        ball.bounce_y()

    # hits paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() <-320:
        ball.bounce_x()
        ball_speed *= 0.9

    # R paddle misses
    if ball.xcor() > 360:
        ball_speed = 0.1
        ball.reset_position()
        scorebaord.l_point()

    # L paddle misses
    if ball.xcor() < -360:
        ball_speed = 0.1
        ball.reset_position()
        scorebaord.r_point()

    # Winning statements
    if scorebaord.l_score == 10:
        scorebaord.goto(0,0)
        scorebaord.write('Left Player Wins!', align = 'center', font = ('Courier', 50, 'bold'))
        game_is_on = False

    if scorebaord.r_score == 10:
        scorebaord.goto(0,0)
        scorebaord.write('Right Player Wins!', align = 'center', font = ('Courier', 50, 'bold'))
        game_is_on = False

screen.exitonclick()
