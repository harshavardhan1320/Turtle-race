from turtle import Turtle, Screen
from random import Random



s = Screen()
s.setup(width=500, height=400)
bet = s.textinput(title="Make your bet ", prompt="Which turtle will win the race ?, Enter the colour: ")

colours = ["red", "yellow", "green", "orange", "blue", "grey"]
positions = [100, 60, 20, -20, -60, -100]
r = Random()

all_turtles = []

for turtle_index in range(0, 6):
    t = Turtle()
    t.shape("turtle")
    t.color(colours[turtle_index])
    t.penup()
    t.goto(-230, positions[turtle_index])
    all_turtles.append(t)

is_race_on = False
if bet:
    is_race_on = True
while is_race_on:

    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_race_on = False
            winning = turtles.pencolor()
            if winning == bet:
                print(f"you have won the race")
            else:
                print(f"The {winning} turtle wins the race")
        moves = r.randint(1, 10)
        turtles.speed(3)
        turtles.forward(moves)



s.exitonclick()
