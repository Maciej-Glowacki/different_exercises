x = input('co wybierasz: kamień, papier czy nożyce? ')

import random
lista = ['kamień', 'papier', 'nożyce']
y = (random.choice(lista))
print(y)

if x == y:
    print('Remis')
elif x == 'kamień' and y == 'nożyce':
    print('Kamień wygrywa')
elif x == 'kamień' and y == 'papier':
    print('Kamień przegrywa')
elif x == 'nożyce' and y == 'papier':
    print('Nożyce wygrywają')
elif x == 'nożyce' and y == 'kamień':
    print('Kamień wygrywa')
elif x == 'papier' and y == 'nożyce':
    print('Nożyce wygrywają')
elif x == 'papier' and y == 'kamień':
    print('Papier wygrywa')

