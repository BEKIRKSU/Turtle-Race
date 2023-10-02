from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=700, height=700)
# this method allows us to choose the width and height of the window that will show up. Use keywords
# arguments rather than positional arguments.
user_choice = screen.textinput(title="Who will win?", prompt="which turtle do you think will win? Choose a colour: ")
# This works just like an input so we just assign it to a variable.
print(user_choice)

shell = Turtle()
# We want the turtle to go to the left of the screen, and we will have more turtles which should all go the same place.
# We can do this with the 'goto' method below, and using the width and height we can adjust this. The turtle should go
# to the left, which means an x value of -350 (or a little less) on a graph of 700 width since it starts in the middle.
shell.goto(x=-335, y=0)





screen.exitonclick()