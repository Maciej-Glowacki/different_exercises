from random import randint

def d6(num):
    s = 0
    for i in range(num):
        s += randint(1,6)
    return s

if __name__ == '__main__':
    for _ in range(5):
        print("Testowy rzut:", d6(3))