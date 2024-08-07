from random import randint
# Cabeçalho
print('\t\tMAIOR E MENOR VALORES EM TUPLA')
print('------------------------------------------------------')

# Entrada de dados
tupla = tuple(randint(1,10) for i in range(5))
tupla_ordenada = (sorted(tupla))


# Saída de dados
print('Valores sorteados em ordem crescente:')
print(f'O maior valor sorteado foi {tupla_ordenada[-1]} ')
print(f'O menor valor sorteado foi {tupla_ordenada[0]}')
print(tupla_ordenada)

