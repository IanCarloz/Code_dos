# -*- coding: utf-8 -*-

def es_primo(n):
    list_num_ant = range(2, n)
    for numero in list_num_ant:
        n % numero = 0
        return False
    return True
