"""
Disegna una scala con 3 gradini
"""
import turtle
#Richiesta Alzata e Pedata
alzata = eval(input("Alzata:"))
pedata = eval(input("Pedata:"))

ninja = turtle.Turtle() # Creo la tartaruga
ninja.pensize(8)        # Imposto la dimensione della penna ad 8
ninja.pencolor("violet")# Imposto il colore del tratto
ninja.shape("turtle")   # Cambio grafica al cursore

# Disegno il primo gradino
ninja.left(90)
ninja.forward(alzata)
ninja.right(90)
ninja.forward(pedata)

# Disegno il secondo gradino
ninja.left(90)
ninja.forward(alzata)
ninja.right(90)
ninja.forward(pedata)

# Disegno il terzo gradino
ninja.left(90)
ninja.forward(alzata)
ninja.right(90)
ninja.forward(pedata)

# Cambio colore al cursore solo per
# una questione di visibilità
ninja.pencolor("black")
