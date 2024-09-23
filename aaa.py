import turtle
import random
import time


def initialize_level(level):
    global delay, snake_speed, border_x, border_y
    if level == "easy":
        delay = 0.1
        snake_speed = 20
        border_x = 300
        border_y = 240
    elif level == "average":
        delay = 0.08
        snake_speed = 20
        border_x = 300
        border_y = 240
    elif level == "difficult":
        delay = 0.04
        snake_speed = 20
        border_x = 400
        border_y = 320

screen = turtle.Screen()
screen.title('Python Snake Game')
screen.setup(width=800, height=700)
screen.tracer(0)
screen.bgcolor('lightgreen')


score = 0
delay = 0.1
snake_speed = 20
border_x = 300
border_y = 240


turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-border_x - 10, border_y + 10)
turtle.pendown()
turtle.color('black')
turtle.forward((border_x * 2) + 20)
turtle.right(90)
turtle.forward((border_y * 2) + 20)
turtle.right(90)
turtle.forward((border_x * 2) + 20)
turtle.right(90)
turtle.forward((border_y * 2) + 20)
turtle.penup()
turtle.hideturtle()

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("darkgreen")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30, 30)


old_fruit = []

scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, border_y + 30)
scoring.write("Score: ", align="center", font=("Courier", 24, "bold"))


level_display = turtle.Turtle()
level_display.speed(0)
level_display.color("black")
level_display.penup()
level_display.hideturtle()
level_display.goto(0, border_y + 60)
level_display.write("Level: Easy", align="center", font=("Courier", 24, "bold"))


def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")


while True:
    screen.update()

    if snake.distance(food) < 20:
        x = random.randint(-border_x + 20, border_x - 20)
        y = random.randint(-border_y + 20, border_y - 20)
        food.goto(x, y)
        score.clear()
        sc += 1
        score.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))

        

        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('circle')
        new_fruit.color('red')
        new_fruit.penup()
        old_fruit.append(new_fruit)

    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()
        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)

    snake_move()

    if snake.xcor() > border_x or snake.xcor() < -border_x or snake.ycor() > border_y or snake.ycor() < -border_y:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('lightgreen')
        scoring.goto(0, 0)
        scoring.write("GAME OVER \n Your Score is {}".format(score), align="center", font=("Courier", 30, "bold"))
        break

    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('lightgreen')
            scoring.goto(0, 0)
            scoring.write("GAME OVER \n Your Score is {}".format(score), align="center", font=("Courier", 30, "bold"))
            break

    time.sleep(delay)
