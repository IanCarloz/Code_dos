# -*- coding: utf-8 -*-

# lista_valores = [10, 100, 90.9 100]
# suma_total / numero_elementos
def promedio():
    promedio = sum(lista_valores) / len(lista_valores)
    return promedio

def moda(lista_valores):
    valores = {}
    for valor in lista_valores:
        if valores.get(valor):
            valores[valor] += 1
        else:
            valores[valor] = 1

    # print(valores)

    v_max = 0
    moda = 0

    for valor, repeticiones in valores.iteritems():
        if repeticiones > v_max:
            v_max = repeticiones
            moda = valor

    return moda

def mediana(lista_valores):
    # ordenar lista
    # detect par o impar
    # par: devolver promedio de centrales
    # impar: valor central

    lista_valores.sort()
    n = len(lista_valores)

    if n % 2:
        return lista_valores[n/2]
    else:
        return (lista_valores[n/2] + lista_valores[n/2 - 1])/2.0

lista_valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mediana(lista_valores))
