nome = str(input('Qual o seu nome? '))
if nome == 'William':
    print(f'Olá, {nome}, Seja bem vindo!')
    print('Calcule sua média de notas: ')
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1 + n2) / 2
    print(f'Sua média é {media:.1f}')
    if media >= 7:
        print('Parabéns, você foi aprovado!')
    else:
        print('Você foi reprovado!')
else:
    print(f'{nome}, seu nome não foi reconhecido no nosso sistema!')