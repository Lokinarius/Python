# Cabeçalho
print('\t\tVALORES ÚNICOS EM UMA LISTA')
print('-' * 20)

# Variaveis
lista = []

# Entrada de dados
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    continua = input('Deseja continuar? ').strip().upper()
    while continua not in ['S', 'N']:
        print('Valor invalido! Digite S para continuar ou N para parar')
        continua = input('Deseja continuar? ').strip().upper()
    if continua == 'N':
        break
# Apresentando os valores em ordem crescente
lista_ordenada = lista.sort()

# Saída de dados
print('-' * 20)
print(f'Você digitou os valores {lista_ordenada}')