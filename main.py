'''
1. Creating a snake body
2. Move the snake
3. Control the snake
4. Detect collision with food
5. Create a scoreboard
6. Detect collision with wall
7. Detect collision with tail

By the end of the project, we should stay with 3 classes: snake class, food class and Scoreboard
'''

from snake import Snake
import time
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard

screen= Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
#screen.tracer(0)

# 1. Creating a snake body

snake=Snake()
food=Food()
scoreboard=ScoreBoard()

screen.listen() #start listening for keystrokes
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# 2. Move the snake 
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move_snake()
     #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  
        snake.extend()
        scoreboard.increase_score()


    #Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.body_snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on=False
            scoreboard.game_over()
    #if head collites with any segment in the tail:
        #trigger game_over

screen.exitonclick()

# 3. Class inheritance

   