import random

rows = random.randint(5, 15)
columns = random.randint(5, 15)

print('Wartość zmiennej rows: ', rows)
print('Wartość zmiennej columns: ', columns)

for x in range(rows):
    print('*' * columns)