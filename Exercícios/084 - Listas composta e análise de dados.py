# Cabeçalho
print('\t\tAnálise de dados')
print('---------------------------------')

# Variaveis
pessoas = []
n = 0

# Entrada de dados
while True:
    n += 1
    nome = (str(input(f'Diga o nome da {n}ª pessoa: ')))
    peso = (float(input(f'Informe o peso {n}ª pessoa: ')))

    # Adicionando dados à lista
    pessoas.append([nome, peso])

    # Verificação de peso
    pesados = []
    for p in pessoas:
        if p[1] >= 100:
            pesados.append(p[0])
    # Também é pssível utilizar uma lista comprehension, como no exemplo abaixo
    # [p[0] for p in pessoas if p[1] >= 100]
    leves = []
    for p in pessoas:
        if p[1] < 50:
            leves.append(p[0])

    # Verificação de continuação
    continua = input('Deseja adicionar outra pessoa? ').strip().upper()
    while continua not in ['S', 'N']:
        print('Valor inválido! Digite S para continuar ou N para parar')
        continua = input('Deseja adicionar outra pessoa? ').strip().upper()
    if continua == 'N':
        break

# Saída de dados
print('--------------------------------')
print('\nResultados:')
print(f'Ao todo foram cadastradas {n} pessoas.')
print(f'O nome das pessoas acima de 100kg são: {", ".join(pesados)}.')
print(f'O nome das pessoas abaixo de 50kg são: {", ".join(leves)}.')
