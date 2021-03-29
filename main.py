from turtle import Turtle, Screen

screen = Screen()

tim = Turtle()
colors = ["orange", "red", "pink", "yellow", "blue", "green"]
tim.speed(0)
screen.bgcolor("black")
screen.setup(1000, 500)

for x in range(360):
    tim.pencolor(colors[x % 6])
    tim.width(x / 5 + 1)
    tim.forward(x)
    tim.left(20)

screen.exitonclick()