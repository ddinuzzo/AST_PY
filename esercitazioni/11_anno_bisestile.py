anno = int(input("Inserisci anno:"))
if anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0):
    print("l'anno", anno, "è bisestile")
else:
    print("l'anno", anno, "non è bisestile")
