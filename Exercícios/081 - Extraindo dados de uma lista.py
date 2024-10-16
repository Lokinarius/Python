# Cabeçalho
print('\t\tEXTRAINDO DADOS DE UMA LISTA')
print('---------------------------------')

# Variaveis
lista = []

# Entrada de dados
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    continua = input('Deseja continuar? ').strip().upper()
    while continua not in ['S', 'N']:
        print('Valor invalido! Digite S para continuar ou N para parar')
        continua = input('Deseja continuar? ').strip().upper()
    if continua == 'N':
        break
# Ordenando a lista de forma decrescente
lista.sort(reverse=True)

# Saída de dados
print('-=' * 10)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 não foi encontrado na lista!')