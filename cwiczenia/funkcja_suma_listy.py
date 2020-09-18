def suma(numbers):
    buff = []
    for num in numbers:
        buff.append(num)
        result = sum(buff)
    return result

l = suma([1, 2, 3, 4, 10])
print(l)