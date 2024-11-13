"""
103
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

"""

# CABEÇALHO
print('Ficha do Jogador')
print("-="*15)

def ficha(nome='Desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s).')

# Chamada da função
nome = str(input('Nome do jogador: ')).capitalize()
gols = input('Quantos gols ele marcou: ')

# Verifica se o valor dos gols foi informado, caso contrário, assume 0
if gols.isdigit():
    gols = int(gols)
else:
    gols = 0

# Chama a função com os valores informados
ficha(nome, gols)


