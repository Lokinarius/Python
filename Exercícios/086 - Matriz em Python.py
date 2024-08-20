# Cabeçalho
print('\t\tMATRIZ')
print('---------------------------------')

# Variaveis
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# Entrada de dados
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor da posição [{i+1},{j+1}]: '))


# Saída de dados
print('---------------------------------')
print('Matriz:')
for i in range(3):
    print(matriz[i])
