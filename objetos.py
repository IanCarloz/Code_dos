# -*- coding: utf-8 -*-

class Animal:
    n_patas = 4
    color = 'negro'
    sonido = ''

    def hacer_sonidos(self):
        print(self.sonido)

    def correr(self):
        print('Run.......')

perro = Animal()
gato = Animal()
print(perro.color)
perro.sonido = 'guau guau!'
perro.hacer_sonidos()
