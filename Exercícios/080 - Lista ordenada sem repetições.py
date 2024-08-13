# Cabeçalho
print('\t\tLISTA ORDENADA SEM REPETIÇÕES')
print('---------------------------------')

# Variaveis
lista = []
i = 0

# Entrada de dados
while len(lista) < 5:
    i += 1
    num = int(input(f'Informe o {i}º número: '))
    if num not in lista:
        # Encontrar a posição para inserir o número na lista
        pos = 0
        while pos < len(lista) and lista[pos] < num:
            pos += 1
        lista.insert(pos, num) #Insere o número na posição correta

# Saída de dados
print('-' * 20)
print(f'Os valores digitados em ordem são: {lista}')

