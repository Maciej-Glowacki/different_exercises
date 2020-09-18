def mean(numbers):
    buff = []
    for num in numbers:
        buff.append(num)
        result = sum(buff)
        result2 = result / len(buff)
    return result2

l = mean([1, 2, 3, 4, 22])
print(l)

# versja 2

def srednia(numbers):
    x = sum(numbers) / len(numbers)
    return x
print(srednia([2, 2, 4, 4]))