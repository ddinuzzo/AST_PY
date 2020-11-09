"""
Applicazione per determinare se un numero passato
in input è pari o dispari.
"""
n = int(input("Inserire un intero:"))
if n % 2 == 0:
    print("il numero", n, "è pari")
else:
    print("il numero", n, "è dispari")
