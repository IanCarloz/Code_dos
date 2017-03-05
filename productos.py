# -*- coding: utf-8 -*-

class Producto:
    precio = 0
    calidad = "Buena"
    origen = ""
    sku = ""
    nombre = ""
    imagen = ''

    # Constructor
    def __init__(self, nombre, sku, precio):
        self.nombre = nombre
        self.sku = sku
        self.precio = precio
        # print('estoy creando un producto')

    def establecer_imagen(self, imagen):
        # busca imagen
        # guarga con nombre
        self.imagen = imagen

class ProductoFisico(Producto):
    fecha_de_caducidad = ""

    def esta_caduco(self):
        return True


class ProductoVirtual(Producto):
    tamano_mb = 0.0

tele = ProductoFisico(nombre='tv sony', sku='123405', precio=109.7)
# print(tele.nombre)
# print(tele.sku)
# print(tele.precio)
