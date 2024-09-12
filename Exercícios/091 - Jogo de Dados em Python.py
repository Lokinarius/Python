#Bibliotecas
from random import randint
from time import sleep
from operator import itemgetter

# Cabeçalho
print('JOGO DE DADOS')
print('--------------')

# Entrada de dados
jogo = {
    f'jogador {i+1}': randint(1,6) for i in range(4)
    }
ranking = dict()
# Saída de dados
for k, v in jogo.items():
    print(f'{k}: tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos')

