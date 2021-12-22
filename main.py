from turtle import Screen
import time
import snake
import food
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake_Game")
screen.tracer(0)


snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grew_up()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    for a in range(1, len(snake.segments)):
        if snake.head.distance(snake.segments[a]) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
