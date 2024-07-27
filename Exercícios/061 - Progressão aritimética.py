# Cabeçalho
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('\t\tGERADOR DE P.A.')
print('=-=-=-=-=-=--=-=-=-=-=-=-=--=-=-=-=-=-=-')

# Entrada de dados
a1 = float(input('Informe o primeiro termo da progressão aritmética: '))
r = float(input('Informe a razão da progressão aritmética: '))
n = int(input('Informe o número de termos: '))

# Cálculo do último termo
an = a1 + (n - 1) * r

# Exibição de termos
print('\nProgressão Aritmética:')
while True:
    print(f'{a1},', end=' ')
    a1 += r
    if a1 > an:
        break
