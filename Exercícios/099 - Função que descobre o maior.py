"""
099
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(primeiro, segundo):
    if primeiro > segundo:
        return primeiro
    else:
        return segundo

primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
print(maior(primeiro, segundo) + "É o maior número")