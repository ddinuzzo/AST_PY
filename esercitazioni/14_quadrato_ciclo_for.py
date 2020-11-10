"""Disegna un quadrato utilizzando un ciclo for"""
import turtle
t = turtle.Turtle()
t.pencolor("blue")
for i in range(4):
    t.forward(150)
    t.left(90)
