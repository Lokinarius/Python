import random
from time import sleep
escolha = ['pedra', 'papel', 'tesoura']
escolha_num = {1: 'pedra', 2: 'papel', 3: 'tesoura'}
jogador = int(input('Escolha 1 para pedra, 2 para papel ou 3 para tesoura: '))
jogador_nome = escolha_num[jogador]
print('---------------------------------')
sleep(1)
print('O computador irá fazer uma jogada... ')
sleep(1)
print('--------------------------------')
sleep(1)
print('JO-KEN-PÔ!')
sleep(1)
maquina_nome = random.choice(escolha)
print('Sua vez!')
print(f'Você escolheu {jogador_nome}')
print(f'O computador escolheu {maquina_nome}')
if jogador_nome == maquina_nome:
    print('Empate!')
elif (jogador_nome == 'pedra' and maquina_nome == 'tesoura') or \
     (jogador_nome == 'tesoura' and maquina_nome == 'papel') or \
     (jogador_nome == 'papel' and maquina_nome == 'pedra'):
    print('Você ganhou!')
else:
    print('Você perdeu!')
