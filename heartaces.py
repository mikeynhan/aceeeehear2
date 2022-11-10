import turtle
win = turtle.Screen()
t = turtle.Turtle()
win.delay(0.2)

def corner():
    for a in range(90):
        t.left(1)
        t.forward(1)

#draw the outline of the card
t.pensize(2)
t.penup()
t.setpos(-191.0,210.0)
t.pendown()
t.setheading(270)
for i in range(2):
    t.forward(400)
    corner()
    t.forward(200)
    corner()

#draw the letter A
t.pensize(1)
t.penup()
t.setpos(-170.0,203.0)
t.pendown()
t.color('red')
t.begin_fill()
t.setpos(-149.0,243.0)
t.setpos(-129.0,203.0)
t.setpos(-138.0,203.0)
t.setpos(-149.0,233.0)
t.setpos(-160,203)
t.setpos(-170,203)
t.end_fill()
t.pensize(3)
t.penup()
t.setpos(-153,220)
t.pendown()
t.setheading(0)
t.forward(13)

#draw the reverse letter A
t.pensize(1)
t.penup()
t.setpos(95,-185)
t.begin_fill()
t.pendown()
t.setpos(74,-225)
t.setpos(54,-185)
t.setpos(64,-185)
t.setpos(74,-215)
t.setpos(85,-185)
t.setpos(96,-185)
t.end_fill()
t.penup()
t.pensize(3)
t.setpos(81,-201)
t.setheading(180)
t.pendown()
t.forward(13)

#draw the hearts
t.penup()
t.setpos(-38,-72)
t.setheading(90)
t.pendown()
t.begin_fill()

def bigheartcurve():
    for j in range(99):
        t.forward(2)
        t.right(2)

t.left(45)
t.forward(115)
bigheartcurve()
t.left(120)
bigheartcurve()
t.forward(120)

t.end_fill()

t.penup()
t.setpos(-150,157)
t.setheading(90)
t.pendown()
t.begin_fill()
def smallheartcurve():
    for q in range(99):
        t.forward(0.4)
        t.right(2)

t.left(45)
t.forward(24)
smallheartcurve()
t.left(120)
smallheartcurve()
t.forward(25)

t.end_fill()

t.penup()
t.setpos(73.0,-139.0)
t.setheading(270)
t.pendown()
t.begin_fill()

def reversecurver():
    for a in range(99):
        t.forward(0.4)
        t.left(2)

t.right(45)
t.forward(24)
reversecurver()
t.right(120)
reversecurver()
t.forward(25)
t.end_fill()

#draw the lightning

t.penup()
t.pensize(20)
t.setpos(-4,152)
t.color("yellow")
t.pendown()
t.setpos(-100,3)
t.setpos(17,73)
t.setpos(-75,-113)


#draw the second aces outline

t.pensize(2)
t.color("black")
t.penup()
t.setpos(-192.0,196.0)
t.pendown()
t.setheading(180)
t.begin_fill()
t.forward(200)
corner()
t.forward(400)
corner()
t.forward(200)
corner()
t.forward(15)

















t.ht()
# win.exitonclick()
# function to find the coordinate:
def buttonclick(x,y):
  print("You clicked at this coordinate({0},{1})".format(x,y))
turtle.onscreenclick(buttonclick,1)
turtle.listen()
turtle.done()