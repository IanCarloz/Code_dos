# -*- coding: utf-8 -*-
# list comprehesion

lista = range(11)

z = [n*n for n in lista if n % 2 == 0]

grupo = ['hector', 'ivan', 'patricio']

x = [n.capitalize() for n in grupo]

print(x)
