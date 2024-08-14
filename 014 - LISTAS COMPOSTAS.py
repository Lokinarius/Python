# LISTAS COMPOSTAS

# PRIMEIRA FORMA DE CRIAR UMA LISTA COMPOSTA
# Primeira pessoa
print('primeira lista: ')
pessoa = list()
pessoa.append('William')
pessoa.append(28)
pessoa.append('M')
pessoa.append(78.9)
# Adicionando primeira pessoa na lista composta
galera = list()
galera.append(pessoa[:])
# Segunda pessoa
pessoa[0] = 'Maria'
pessoa[1] = 26
pessoa[2] = 'F'
pessoa[3] = 65.2
# Adicionando segunda pessoa na lista composta
galera.append(pessoa[:])
# Saída de dados
print(galera)


# SEGUNDA FORMA DE CRIAR UMA LISTA COMPOSTA
print('\n----------------------------------------------------------------')
print('Segunda lista: ')
galera2 = [['João', 19], ['Ana', 24], ['Fernando', 20], ['Alfredo', 31]]
print(f'Utilizando uma saída como "print(galera2[0][0])" a saída será o nome do primeiro elemento que é'
      f' {galera2[0][0]}')
print(f'Utilizando uma saída como "print(galera2[0][1])" a saída será a idade do primeiro elemento que '
      f'é {galera2[0][1]}')

# OUTRA FORMA DE SAÍDA DAS LISTAS COMPOSTAS
for p in galera2:
    print(f'Nome: {p[0]}, Idade: {p[1]}')

# OBTENÇÃO DE DADOS
print('\n----------------------------------------------------------------')
print('Obtendo dados:')
galera3 = list()
dado = list()
for c in range(3):
    dado.append(str(input(f'Nome da {c+1}ª pessoa : ')))
    dado.append(int(input(f'Idade da {c+1}ª pessoa : ')))
    galera3.append(dado[:])
    dado.clear()
for p in galera3:
    print(f'Nome: {p[0]}, Idade: {p[1]}')