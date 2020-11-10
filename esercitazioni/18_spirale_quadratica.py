import turtle
dimension = 10
space = 10
spire = 30
t = turtle.Turtle()
for i in range(spire):
    if i != 0:
        dimension += space
        t.left(90)
    t.forward(dimension)
