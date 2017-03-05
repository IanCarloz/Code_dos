# -*- coding: utf-8 -*-
# checkout
# __init__.py
from productos import ProductoFisico
from metodos import Bitcoin,Stripe

class Checkout:

    def __init__(self, metodo_de_pago):
        self.metodo_de_pago = metodo_de_pago

    def obtener_total(self, lista_productos):
        total = 0
        for Producto in lista_productos:
            total += Producto.precio
        return total

    def imprimir_lista(self, lista_productos):
        # imprimir productos con su sku, precio y total
        for producto in lista_productos:
            print('Nombre: %s, Sku: %s, Precio: %s' % (producto.nombre, producto.sku, producto.precio))

    def cobrar(self, lista_productos):
        total = self.obtener_total(lista_productos)
        self.metodo_de_pago.cobrar(total)
        print('He cobrado %s' % total)

tele = ProductoFisico('tele', '100', 100)
Radio = ProductoFisico('Radio', '101', 50)
Computadora = ProductoFisico('Computadora', '105', 1000)
lista_productos = [tele, Radio, Computadora]

# stripe = Bitcoin()
checkout_stripe = Checkout(Stripe)
checkout_stripe.cobrar(lista_productos)
# checkout = Checkout()
# lista_productos = [
#     ProductoFisico('tele', '100', 100),
#     ProductoFisico('Radio', '101', 50),
#     ProductoFisico('Computadora', '105', 1000)
# ]
# print(checkout.obtener_total(lista_productos))
