# -*- coding: utf-8 -*-

def precio_final(precio=0, tasa_iva=0.15):
    return precio * (1 + tasa_iva)

p = 10000
#t = 0.16

#print(precio_final(p, tasa_iva=0.16))

# args es una lista [] de todos los parametros que recibe
def imprimir_lista_de_productos(*args):
    for producto in args:
        print(producto)

def aplicar_impuestos(precio, **kwargs):
    impuestos = []
    for key, value in kwargs.iteritems():
        total = precio * value
        impuestos.append(total)
        print('de %s son: %s' % (key, total))
    total = precio + sum(impuestos)
    print ('Precio inicial: %s mas impuestos: %s' % (precio, total))

def impuestos2(precio, **kwargs):
    total_impuestos = 0
    for impuesto, tasa in kwargs.iteritems():
        impuesto_actual = precio * tasa
        total_impuestos = total_impuestos + impuesto_actual
        print(impuesto + " es " + str(impuesto_actual))
        print(total_impuestos)
    return precio + total_impuestos

#imprimir_lista_de_productos('a', 'b', 'c')
#aplicar_impuestos(1000, iva=0.16, ips=0.04, isr=0.18)
impuestos2(1000, iva=0.16, ips=0.04, isr=0.18)
