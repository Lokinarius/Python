# Cabeçalho
print('-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('\t\tSUPER GERADOR DE P.A.')
print('-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

while True:
    # entrada de dados
    a1 = float(input('Informe o primeiro termo da progressão aritmética: '))
    r = float(input('Informe a razão da progressão aritmética: '))
    n = int(input('Informe o número de termos: '))
    if n <= 0:
        print('O número de termos deve ser maior que zero')
        break

    # Variaveis
    an = a1 + (n - 1) * r
    atual = a1
    total = 0

    # Exibição dos termos
    while True:
        print('\nProgressão aritmética: ')
        for c in range(n):
            print(f'{atual},', end=' ')
            atual += r
            total += 1
        print('\npausa')

        mais = int(input('Quantos termos você deseja adicionar? '))
        if mais <= 0:
            print('FIM')
            break
        else:
            n = mais
    break
print(f'Progressão finalizada com {total} de termos mostrados.')

