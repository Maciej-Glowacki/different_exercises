def to_celcius(fahrenheit):
    c = ((fahrenheit - 32) * 5) / 9
    return c

celcius = to_celcius(42)
print(round(celcius, 2),)