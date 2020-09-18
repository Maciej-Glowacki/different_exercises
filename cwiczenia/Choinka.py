import random
size = random.randint(3, 9)
print ('Wielkość choinki: ', size)

i = 1
while i <= size:
    print('*' * i)
    i += 1
    
import random
size = random.randint(3, 9)

print('Wielkość choinki: ', size)
i = 1
for x in range(size):
    print(i * '*')
    i += 1
