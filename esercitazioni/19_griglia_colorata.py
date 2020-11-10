import turtle

colori = ("green", "red", "blue", "yellow", "purple", "lightblue")
box_dimension = 30
pensize = 5
cell_space = pensize + 2

t = turtle.Turtle()
s = turtle.Screen()
s.title("Griglia Colorata")
row_num = int(s.numinput("Numero di righe", "Righe:"))

t.pensize(pensize)
y_offset = 0
for colore in colori:
    t.pencolor(colore)
    for idx in range(row_num):
        t.pendown()
        for l in range(4):
            t.forward(box_dimension)
            t.right(90)
        t.penup()
        t.seth(-90)
        y_offset += box_dimension + cell_space
        t.forward(box_dimension + cell_space)
        t.seth(0)
    t.forward(box_dimension + cell_space)
    t.seth(90)
    t.forward(y_offset)
    y_offset = 0
    t.seth(0)
