# Lewis Wilson
# 27 March 2024
# P4LAB1B
# A turtle drawing initials

import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Hello!")

# Meet Alex the turtle, he will draw my initials!

alex = turtle.Turtle()
alex.color("purple")
alex.shape("turtle")
alex.pensize(3)

# Let's draw the first initial "L"!
alex.penup()
alex.left(180)
alex.forward(200)
alex.right(90)
alex.forward(150)
alex.right(180)
alex.pendown()
alex.forward(150)
alex.left(90)
alex.forward(100)
alex.penup()
alex.forward(60)

# Let's draw the next initial "W"!
alex.left(110)
alex.forward(160)
alex.left(180)
alex.pendown()
alex.forward(160)
alex.left(130)
alex.forward(90)
alex.right(120)
alex.forward(90)
alex.left(130)
alex.forward(160)

# Let's move Alex out of the way...
alex.penup()
alex.right(130)
alex.forward(90)
alex.right(120)


wn.mainloop()
