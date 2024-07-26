# BIBLIOTECAS
import random

# CABEÇALHO
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\t\tJOGO DE ADIVINHAÇÃO 2.0')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

# ENTRADA DE DADOS
print('O computador pensou em um número entre 1 e 100, tente adivinhar')
print('================================================================')
number = random.randint(1, 100)
guess = 0
num = int(input('Chute um número: '))
while True:
    guess += 1
    if num == number:
        print(f'Você acertou! O número é {number}')
        print(f'Você precisou de {guess} tentativas para acertar o número.')
        break
    elif num != number:
        if num < number:
            print(f'Você errou! O número é maior que {num}.')
        else:
            print(f'Você errou! O número é menor que {num}.')
        num = int(input('Chute um número: '))
