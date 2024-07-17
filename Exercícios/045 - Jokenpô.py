import random
print('JOKENPÔ')
print('---------------------------------')
print('O computador irá fazer uma jogada... ')
print('--------------------------------')
choices = ['pedra', 'papel', 'tesoura']
computer_choice = random.choice(choices)
print('Sua vez!')
player_choice = input('Escolha entre pedra, papel ou tesoura: ').lower()
if player_choice == computer_choice:
    print(f'O computador escolheu {computer_choice}')
    print('Empate!')
elif player_choice == ['pedra']:
    if computer_choice == ['tesoura']:
        print(f'O computador escolheu {computer_choice}')
        print('Você ganhou!')
    else:
        print(f'O computador escolheu {computer_choice}')
        print('Você perdeu!')
elif player_choice == ['tesoura']:
    if computer_choice == ['papel']:
        print(f'O computador escolheu {computer_choice}')
        print('Você ganhou!')
    else:
        print(f'O computador escolheu {computer_choice}')
        print('Você perdeu!')
elif player_choice == ['papel']:
    if computer_choice == ['pedra']:
        print(f'O computador escolheu {computer_choice}')
        print('Você ganhou!')
    else:
        print(f'O computador escolheu {computer_choice}')
        print('Você perdeu!')