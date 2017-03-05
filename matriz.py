# -*- coding: utf-8 -*-
m = input('matriz')
def matriz_identidad(n):
    """Devuelve una lista de listas que representa una
       matriz identidad de tamaño n."""
    return [[(1 if ren == col else 0) for col in range(n)]
            for ren in range(n)]
print matriz_identidad(m)
