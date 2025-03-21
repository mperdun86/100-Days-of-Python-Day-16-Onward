from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forwards():
    tom.forward(10)

def move_backwards():
    tom.back(10)

def turn_left():
    tom.left(10)

def turn_right():
    tom.right(10)

def screen_clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(key = "c", fun = screen_clear)
screen.exitonclick()