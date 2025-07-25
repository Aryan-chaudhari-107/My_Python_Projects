
from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.bgcolor("black")
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
print(user_bet)

colour = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y = y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on  = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is winner!")

        random_dist = random.randint(0,10)
        turtle.forward(random_dist)


screen.exitonclick()

# Draw is unfinished