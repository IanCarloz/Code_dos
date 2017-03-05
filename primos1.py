ini = 0
fin = 30

def es_primo(n):
    if n < 2 or n%2 == 0 and n != 2:
        return False
    for y in range(3, n):
        if n%y == 0:
            return False
    print n
    return n

def calcular():
    x = input('Numero?')
    # es_primo(x)
    print es_primo(x)

# calcular()

def primos():
    fin = input('lim?')
    for i in range(ini, fin):
        es_primo(i)
primos()

def primeros(p):
    pr = []
    out = 0
    while p < len(pr):
        for x in range(out):

            out += 1
    # while p < primos:
    #     if n < 2 or n%2 == 0 and n != 2:
    #         return False1
