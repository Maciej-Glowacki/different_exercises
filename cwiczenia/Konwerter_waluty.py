def convert_to_usd(zlotys):
    result = zlotys / 3.85
    return result

wynik = convert_to_usd(300)
print(wynik)

def convert_to_usd(zlotys, rate = 3.85):
    result = zlotys / rate
    return result

wynik = convert_to_usd(1200)
print(wynik)

def convert_to_usd(zlotys, rate = 3.85):
    result = round((zlotys / rate), 2)
    return result

wynik = convert_to_usd(1500)
print(wynik)