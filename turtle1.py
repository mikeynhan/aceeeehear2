import turtle
win=turtle.Screen()
t=turtle.Turtle()
t.bgcolor("red")






# win.exitonclick()
# function to find the coordinate:
def buttonclick(x,y):
  print("You clicked at this coordinate({0},{1})".format(x,y))
turtle.onscreenclick(buttonclick,1)
turtle.listen()
turtle.done()