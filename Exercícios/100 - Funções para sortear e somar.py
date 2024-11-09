# [IMPORTS]
import random
from time import sleep

# [CABEÇALHO]
print("Gerador de Números Randomicos")
print("=" * 30)

def sorteia(lista):
    for contador in range(0, 5):
        numero = random.randint(1, 100)
        lista.append(numero)
        print(f'{numero}', end='')
        sleep(0.5)
def somaPar(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(f'A soma dos valores pares é {soma}')

# [Saída]
numeros = list()
sorteia(numeros)
somaPar(numeros)


