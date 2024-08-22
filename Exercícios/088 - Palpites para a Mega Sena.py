# Bibliotecas
from random import randint

# Cabeçalho
print('---------------------------------')
print('\t\tMEGA SENA')
print('---------------------------------')

# Variaveis
jogos = []

# Entrada de dados
jogadas = int(input('Quantos jogos você quer que eu sorteie? '))

for n in range(jogadas):
    jogo = []
    jogo.clear()
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            jogo.sort()
    jogos.append(jogo)

# Saída de dados
for j in range(jogadas):
    print(f'Jogo {j+1}: {jogos[j]}')
