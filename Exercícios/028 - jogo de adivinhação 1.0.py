import random
numero = random.randint(1,10)
num = int(input('Em que número a máquina pensou? '))
if num == numero:
    print('Parabéns, você acertou!')
else:
    print(f'Infelizmente, você errou, o número era {numero}. Tente novamente.')