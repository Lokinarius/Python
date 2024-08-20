# Cabeçalho
print('\t\tMATRIZ')
print('---------------------------------')

# Variaveis
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

# Entrada de dados
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o elemento [{i+1},{j+1}]: '))
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        if j == 2:
            soma_terceira_coluna += matriz[i][j]
        if i == 1 and matriz[i][j] > maior_segunda_linha:
            maior_segunda_linha = matriz[i][j]


# Saída de dados
print('\n---------------------------------')
print('Matriz:')
for i in range(3):
    print(matriz[i])
print('\n---------------------------------')
print(f'A soma de todos os valores pares é de {soma_pares}')
print(f'A soma dos valores da terceira coluna é de {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')
