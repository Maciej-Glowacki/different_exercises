import random

lst = ['krok', 'korek', 'kora', 'roraty', 'kran', 'rota', 'mirra']

x = random.choice(lst)
y = x.split()
z = random.shuffle(y)
q = z.join
print(q)

