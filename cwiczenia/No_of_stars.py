import random
size = random.randint(3, 9)

print(size)
i = 1
for x in range(size):
    print(i * '*')
    i += 1