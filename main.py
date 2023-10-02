from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=700, height=700)
# this method allows us to choose the width and height of the window that will show up. Use keywords
# arguments rather than positional arguments.
user_choice = screen.textinput(title="Who will win?", prompt="which turtle do you think will win? Choose a colour: ")
# This works just like an input so we just assign it to a variable.
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
y_positions = [-70, -30, 10, 50, 90, 130]

for turtle_index in range(0,6):
    shell = Turtle(shape="turtle")
    shell.color(colors[turtle_index])
    shell.shapesize(2, 2)
# We can just set the shape when we set the name.
    shell.penup()
# We won't do pen down since it's a race and not a drawing.
# We want the turtle to go to the left of the screen, and we will have more turtles which should all go the same place.
# We can do this with the 'goto' method below, and using the width and height we can adjust this. The turtle should go
# to the left, which means an x value of -350 (or a little less) on a graph of 700 width since it starts in the middle.
    shell.goto(x=-330, y=y_positions[turtle_index])
# Now we can just make more.





screen.exitonclick()