def square(num):
    x = num ** 2
    return x

print(square(5))

def square_print(num):
    print(num ** 2)

num = 11
square_print(num)

a = square(10) + 10
print(a)
b = square_print(10) + 10