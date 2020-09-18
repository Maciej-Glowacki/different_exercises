# n = input ('Podaj liczbę z przedziału 1-10')
# n = int(n)
# for i in range (1,11):
#     print(i, '*', n, '=', i * n)
#

def tabliczka(i,n):
    i= input('podaj liczbe')
    n = range(1,11)
    for n in range(1,11):
        print(i, '*', n, '=', i * n)

print(tabliczka(input, 4))




