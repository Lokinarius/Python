# Cabeçalho
print('\t\tDIVIDINDO VALORES EM VÁRIAS LISTAS')
print('------------------------------------------------------')

# Variaveis
lista = []
lista_pares = []
lista_impares = []

# Entrada de dados
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
    resposta = input('Deseja continuar? (S/N): ').strip().upper()
    while resposta not in ['S', 'N']:
        print('Valor invalido! Digite S para continuar ou N para parar')
        resposta = input('Deseja continuar? ').strip().upper()
    if resposta == 'N':
        break

# Saída de dados
print('-=' * 10)
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {lista_pares}')
print(f'A lista de números ímpares é {lista_impares}')