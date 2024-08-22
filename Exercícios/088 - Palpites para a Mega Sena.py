# Bibliotecas
from random import randint

# Cabeçalho
print('---------------------------------')
print('\t\tMEGA SENA')
print('---------------------------------')

# Variaveis
jogo = list()
# Entrada de dados
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(jogos):
    jogo.clear()
    for n in range(6):
        num = randint(1, 60)
        while num in jogo:
            num = randint(1, 60)
        jogo.append(num)

# Saída de dados
print(f'-=-=-= SOTEANDO {jogos} JOGOS -=-=-=')
for j in range(jogos):
    print(f'Jogo {jogos}: {jogo}')
