# Cabeçalho
print('\t\tESTATÍSTICAS')
print('---------------------------------')

# Variaveis
n = 0
soma = 0.0
total = 0.0
mais_1000 = 0
# float('inf') representa um valor infinito possivel
mais_barato = float('inf')
nome_mais_barato = ''

# Entrada de dados
while True:
    print('\n================================')
    n += 1
    nome = str(input(f'Qual o nome do {n}º Produto? '))
    preco = float(input(f'Qual o preço do {n}º Produto? R$'))
    total += preco
    if preco > 1000:
        mais_1000 += 1
    if preco < mais_barato:
        mais_barato = preco
        nome_mais_barato = nome
    while True:
        continuar = input('Deseja adicionar outro produto? ').strip().upper()
        if continuar in ['S', 'N']:
            break
        else:
            print('Opção inválida! Informe "S" para sim ou "N" para não.')
    if continuar == 'N':
        break

# Resultados
print('\nResultados:')
print(f'Foram cadastrados {n} produtos.')
print(f'O total gasto da compra foi de R${total:.2f}.')
if mais_1000 > 0:
    print(f'Existem um total de {mais_1000} produtos que custam mais de R$1000.')
print(f'O Produto mais barato foi {nome_mais_barato}')


