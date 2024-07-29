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

    # Cálculo do último termo
    an = a1 + (n - 1) * r

    # Exibição dos termos
    print('\nProgressão aritmética: ')
    while True:
        print(f'{a1},', end=' ')
        a1 += r
        if a1 > an:
            break

    # Sair do loop
    continuar = input('\nDeseja gerar outra progressão? (s/n) ').strip().lower()
    if continuar == 'n':
        print('Programa encerrado.')
        break
