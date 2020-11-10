n = int(input("Numero:"))
somma = 0
for i in range(1, n + 1):
    quadrato = i ** 2
    print(quadrato, end="")
    print(" ", end="")
    somma += quadrato
print()
print("Somma dei quadrati:", somma)
