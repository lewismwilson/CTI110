# Lewis Wilson
# 27 March 2024
# P4LAB1A
# Turtles drawing shapes

#initialize
import turtle
win = turtle.Screen()
win.bgcolor("black")

# meet Franklin the turtle. He will draw a rectangle.
franklin = turtle.Turtle()
franklin.shape("turtle")
franklin.color("green")
franklin.pensize(3)

# meet Amanda the turtle. She will draw a triangle.
amanda = turtle.Turtle()
amanda.shape("turtle")
amanda.color("hotpink")
amanda.pensize(3)

# Franklin will now draw a rectangle!
for i in range(4):
    if (i%2 == 0):
        franklin.forward(100)
        franklin.left(90)
    elif (i%2 == 1):
        franklin.forward(50)
        franklin.left(90)

# Let's move Amanda so her triangle doesn't overlap Franklin's rectangle
amanda.penup()
amanda.left(180)
amanda.forward(50)
amanda.pendown()

# Now Amanda will draw her triangle!
for i in range(3):
    amanda.forward(150)
    amanda.right(120)

# Now the turtles will amdire their work!

amanda.penup()
franklin.penup()

amanda.right(180)
franklin.left(180)

amanda.forward(10)
franklin.forward(10)

amanda.right(90)
franklin.left(90)

amanda.forward(50)
franklin.forward(50)

amanda.right(90)
franklin.left(90)

amanda.forward(85)
franklin.forward(60)

amanda.right(90)
franklin.left(90)

amanda.stamp()
franklin.stamp()

amanda.forward(95)
franklin.forward(75)

amanda.right(180)
franklin.left(180)


# At the end, keep the window open until closed
win.mainloop()
