import random

no_of_stars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]

random_number = random.randint(0,20)
random_star = '*' * random_number
print('Wylosowana liczba: ', random_number)
print(random_star)