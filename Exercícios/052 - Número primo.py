# Cabeçalho
print('\t\tNÚMERO PRIMO')
print('--------------------------------')

# Entrada de dados
num = int(input('Informe um número: '))
tot = 0

# Verifica se o número é primo
print(f'Analisando o número {num}: ')
for c in range(1, num + 1):
    if num % c == 0:
        print(f'[{c}]', end=' ')
        tot += 1
    else:
        print(f'{c}', end=' ')

# Resultado
print(f'\nO número {num} foi divisivel {tot} vezes.')
if tot == 2:
    print('Logo ele é um número primo!')
else:
    print('Logo ele não é um número primo!')