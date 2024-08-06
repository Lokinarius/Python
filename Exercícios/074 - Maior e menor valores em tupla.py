from random import randint
# Cabeçalho
print('\t\tMAIOR E MENOR VALORES EM TUPLA')
print('------------------------------------------------------')

# Entrada de dados
tupla = tuple(randint(1,10) for i in range(5))

# Saída de dados
print('Valores sorteados em ordem crescente:')
print(sorted(tupla))
