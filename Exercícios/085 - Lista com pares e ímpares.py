# Cabeçalho
print('\t\tNUMEROS PARES E ÍMPARES')
print('-' * 20)

# Variaveis
numero = []
pares = []
impares = []

# Entrada de dados
for i in range(7):
    numero.append(int(input(f'Digite o {i+1}º número: ')))
    if numero[i] % 2 == 0:
        pares.append(numero[i])
    else:
        impares.append(numero[i])

# Ordenando listas
pares.sort()
impares.sort()

print('-' * 20)
print(f'Os valores pares digitados em ordem foram: {pares}')
print(f'Os valores ímpares digitados em ordem foram: {impares}')