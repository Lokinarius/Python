"""
103
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

"""

# CABEÇALHO
print('Ficha do Jogador')
print("-="*15)

def ficha():
nome = str(input('Nome do jogador: ')).capitalize()
gols = int(input('Quantos gols ele marcou: '))


