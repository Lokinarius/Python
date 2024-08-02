import time
# Cabeçalho
print('\t\tCAIXA ELETRÔNICO')
print('---------------------------------')

# Variaveis
c_50 = 0
c_20 = 0
c_10 = 0
c_1 = 0

# Entrada de dados
valor = int(input('Qual o valor a ser sacado? '))
while True:
    if valor >= 50:
        valor -= 50
        c_50 += 1
    elif valor >= 20:
        valor -= 20
        c_20 += 1
    elif valor >= 10:
        valor -= 10
        c_10 += 1
    elif valor >= 1:
        valor -= 1
        c_1 += 1
    else:
        break

# Saída de dados
print(f'Seu dinheiro está sendo preparado...')
time.sleep(1)
print('---------------------------------')
if c_50 > 0:
    print(f'{c_50} notas de R$50')
if c_20 > 0:
    print(f'{c_20} notas de R$20')
if c_10 > 0:
    print(f'{c_10} notas de R$10')
if c_1 > 0:
    print(f'{c_1} notas de R$1')


