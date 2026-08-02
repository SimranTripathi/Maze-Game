import turtle

screen = turtle.Screen()
screen.title("Maze Game")
screen.bgcolor("lightgreen")
screen.setup(width=700, height=700)

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.color("blue")
pen.hideturtle()

start_positions = [(-200, 250), (-70, 250), (70, 250), (200, 250)]

for i, pos in enumerate(start_positions):
    pen.penup()
    pen.goto(pos)
    pen.write(str(i + 1), align="center", font=("Arial", 14, "bold"))

paths = [
    [(-200, 250), (-200, 100), (-100, 0), (0, -100)],
    [(-70, 250), (-50, 100), (50, 50), (100, -100)],
    [(70, 250), (80, 100), (0, 50), (-50, -100)],
    [(200, 250), (150, 100), (120, 0), (50, -100)]
]

for path in paths:
    pen.penup()
    pen.goto(path[0])
    pen.pendown()

    for point in path[1:]:
        pen.goto(point)

pen.penup()
pen.goto(0, -200)
pen.color("red")
pen.write(" HOME", align="center", font=("Arial", 18, "bold"))

turtle.done()