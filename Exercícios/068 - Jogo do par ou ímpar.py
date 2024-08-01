import random
# Cabeçalho
print('\t\tPAR OU IMPAR')
print('-------------------------------------')

# Declaração de variáveis
acerto = 0

# Entrada de dados
while True:
    print('\n================================')
    num = random.randint(1, 1000)
    par = (num % 2 == 0)
    par_ou_impar = str(input('O número que o computador pensou foi Par ou impar? ')).strip().upper()
    if par_ou_impar not in ['PAR', 'íMPAR', 'IMPAR']:
        print('Resposta inválida! Digite "par" ou "impar')
        continue
    if (par_ou_impar == 'PAR' and par) or (par_ou_impar == 'IMPAR' and not par):
        acerto += 1
    else:
        print(f'Você errou! Mas acertou {acerto} vezes.')
        break
