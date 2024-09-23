import turtle
import time
import random

sc = 0
delay = 0.1

turtleScreen = turtle.Screen()
turtleScreen.title("Snake Game")
turtleScreen.bgcolor("#3b9444")
turtleScreen.setup(width=700, height=750)
turtleScreen.tracer(0)

wall = turtle.Turtle()
wall.pensize(3)
wall.color("black")
wall.penup()
wall.goto(-300,300)
wall.pendown()
wall.forward(600)
wall.penup()
wall.setheading(270)
wall.pendown()
wall.forward(650)
wall.setheading(180)
wall.forward(600)
wall.setheading(90)
wall.forward(650)
wall.hideturtle()

snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("#323aa8")
snake.penup()
snake.goto(-58,0)
snake.direction = 'Stop'

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-288, 288), random.randint(-338, 288))

score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("black")
score.penup()
score.hideturtle()
score.goto(0,320)

body = []

def up():
    if snake.direction != "down":
        snake.direction = "up"
def down():
    if snake.direction != "up":
        snake.direction = "down"
def left():
    if snake.direction != "right":
        snake.direction = "left"
def right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
        score.clear()
    elif snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
        score.clear()
    elif snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)
        score.clear()
    elif snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
        score.clear()


def check_collision():
    if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 280 or snake.ycor() < -338:
        return True
    for segment in body[1:]:
        if segment.distance(snake) < 20:
            return True
    return False

def add_body(sc,delay):
    new_food = turtle.Turtle()
    new_food.speed(0)
    new_food.shape("square")
    new_food.color("#323aa8")
    new_food.penup()
    body.append(new_food)
    delay -= 0.001
    sc += 1

turtleScreen.listen()
turtleScreen.onkeypress(up, "Up")
turtleScreen.onkeypress(down, "Down")
turtleScreen.onkeypress(left, "Left")
turtleScreen.onkeypress(right, "Right")


while True:
    turtleScreen.update()
    time.sleep(0.1)

    if check_collision():
        score.write(" Game Over. Thank you for Playing", align = "center", font = ("Times new roman", 24, "normal"))
        snake.goto(-58,0)
        snake.direction = 'Stop'
        for segment in body:
            segment.goto(1000, 1000)
        body = []
        time.sleep(1)

    if snake.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        add_body(sc,delay)

    move()

    for i in range(len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)
    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)

    
