from libreria.core import Libreria
from libreria.models import Book, Dvd, Magazine, Product

# Istanzio un oggetto libreria
libreria = Libreria()
# Aggiungo una serie di libri con relativa quantità alla libreria
libreria.add(Book(1, 'Guerra e pace', 'Lev Nikolaevic Tolstoj', '10.00'), 10)
libreria.add(Book(2, 'Il Processo', 'Franz Kafka', '25.99'), 5)
libreria.add(Book(3, 'Moby Dick', 'Herman Melville', '17.49'), 2)
libreria.add(Book(4, 'Il barone rampante', 'Italo Calvino', '14.50'), 20)
libreria.add(Dvd(5, 'Il Corpo Umano - La Macchina Incredibile', 'Discovery Channel', '10.65'), 5)
libreria.add(Dvd(6, 'Grandi Scoperte Della Scienza', 'Discovery Channel', '29.90'), 2)
libreria.add(Dvd(7, 'Einstein - La Vita E La Scienza', 'Cinehollywood', '9.90'), 1)
libreria.add(Magazine(8, 'Focus', 'Mondadori', '4.90'), 10)
libreria.add(Magazine(9, 'PC - professionale', 'Visibilia', '2.90'), 1)
libreria.add(Magazine(10, 'Einstein - La Vita E La Scienza', 'La Verità srl', '4.90'), 1)

Libreria.print_menu()

print()

while True:
    choise = input('Cosa vuoi fare? ')
    if choise == '1':
        libreria.warehouse()
    elif choise == '2':
        identifier = int(input('Inserire l\'id del prodotto: '))
        libreria.buy(identifier)
    elif choise == '3':
        Libreria.print_menu()
    elif choise == 'q':
        print('Grazie per aver utilizzato il nostro programma')
        break
    else:
        print('Il valore inserito non è valido')
exit(0)
