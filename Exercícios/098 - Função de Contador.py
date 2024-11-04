"""
098
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: inicio, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada
"""

# CABEÇALHO
print("================================")
print("Contador de valores...")
print("================================")

# FUNÇÃO DE CONTAGEM
def contador(inicio,fim,passo):
    for i in range(inicio, fim + 1, passo):
        print(i)

# SAIDA DE DADOS
print("Contagem 1: ")
contador(1, 10, 1)

print("\nContagem 2: ")
contador(10, 0, -2)

print("\nContagem personalizada:")
inicio = int(input("Qual será o início da contagem? "))
fim = int(input("Qual será o fim da contagem? "))
passo = int(input("Qual será o passo da contagem? "))
contador(int(inicio), int(fim), int(passo))
