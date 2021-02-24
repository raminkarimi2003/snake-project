from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.right, key="Right")
screen.onkeypress(fun=snake.left, key="Left")

race_on = True
while race_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if food.distance(snake.head) < 15:  # detect collision
        food.refresh()
        scoreboard.increase_score()
        snake.extend_segment()

    if snake.head.xcor() < -295 or snake.head.xcor() > 295 or snake.head.ycor() < -295 or snake.head.ycor() > 295:
        race_on = False  # game stop (going out of loop)
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            race_on = False  # game stop (going out of loop)

screen.exitonclick()
