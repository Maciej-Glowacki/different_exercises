
Skip to content
Pull requests
Issues
Marketplace
Explore
@Maciej-Glowacki
pka69 /
WAR_PYT_O_01_podstawy_pythona
Private
forked from CodersLab/WAR_PYT_O_01_podstawy_pythona

0
0

    17

Code
Pull requests
Actions
Projects
Security

    Insights

WAR_PYT_O_01_podstawy_pythona/06_Dzien_3_-_praca_domowa/homework.py /
@pka69
pka69 hoework day3, day4 - done
Latest commit 0471e28 10 days ago
History
1 contributor
39 lines (33 sloc) 1.14 KB
import random

def random_average(n = 1):
    try:
        result = sum([random.randint(1,100) for _ in range(n)]) / n
    except ZeroDivisionError as e:
        return None
    return result

def div():
    try:
        a = int(input("Podaj a:"))
        b = int(input("podaj b:"))
        if not a or not b: raise ValueError("któraś z liczb nie jest naturalan (czyli >0)")
        return a / b
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)

check_table = [int(item) for item in ('1 3 7 9 1 3 7 9 1 3'.split(' '))]

def validate_pesel(PESEL):
    try:
        to_check = [int(item) for item in PESEL]
    except  ValueError as e:
        return False
    result = 10 - sum([to_check[i]*check_table[i] for i in range(10)]) % 10
    if result ==10: result = 0
    return result == to_check[10]


if __name__ == "__main__":
    print(random_average(0))
    print("wynik działania a / b:", div())
    print(check_table)
    print("PESEL - 69010108851:", validate_pesel("69010108851"))
    print("PESEL - 69010108850:", validate_pesel("69010108850"))
    print("PESEL - 02321709033:", validate_pesel("02321709033"))

    © 2020 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

