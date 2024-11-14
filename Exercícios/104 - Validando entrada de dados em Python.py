"""
104
Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python.
Só que fazendo a validação para aceitar apenas um valor numérico.

EX:
n= leiaInt('Digite um n')
"""

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('Erro! Digite um número inteiro válido.')



n = leiaInt('Digite um número: ')
