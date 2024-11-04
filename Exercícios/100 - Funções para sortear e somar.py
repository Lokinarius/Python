"""
100
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores PARES sorteados pela função anterior.
"""

import random

def sorteia():
    numeros = []
    for _ in range(5):
        numeros.append(random.randint(1, 100))
    return numeros

def somaPar(numeros):
    return sum(num for num in numeros if num % 2 == 0)
