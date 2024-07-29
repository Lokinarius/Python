# Cabeçalho
print('\t\tSOMA DE VALORES')
print('---------------------------------')

# Variaveis
soma = 0
n = 0

# Entrada de dados
while True:
    print('\n================================')
    num = int(input('Informe um número (ou 999 para sair): '))
    if num == 999:
        break
    soma += num
    n += 1


# resultado da soma
print('\n---------------------------------')
print(f'foram digitados {n} valores, e a soma entre eles é {soma}')