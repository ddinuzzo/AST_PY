"""Stampa tutti i numeri minori di n e divisibili per 3 e 5"""
n = eval(input("Inserisci un numero:"))
i = 1
while i < n:
    if i % 5 == 0 and i % 3 == 0:
        print(i, sep="", end="")
        print(" ", sep="", end="")
    i += 1
