# Cabeçalho
print('\t\tBOLETIM DE NOTAS')
print('-------------------------------------')

# Variáveis
alunos = []

# Entrada de dados
while True:
    print('\n================================')
    nome = input('Nome do aluno: ')

    # Coleta e validação das notas
    while True:
        try:
            n1 = float(input('1ª nota: '))
            if 0 <= n1 <= 10:
                break
            else:
                print('Nota inválida! Digite uma nota entre 0 e 10.')
        except ValueError:
            print('Entrada inválida! Digite um número.')

    while True:
        try:
            n2 = float(input('2ª nota: '))
            if 0 <= n2 <= 10:
                break
            else:
                print('Nota inválida! Digite uma nota entre 0 e 10.')
        except ValueError:
            print('Entrada inválida! Digite um número.')

    media = (n1 + n2) / 2
    alunos.append([nome, n1, n2, media])

    continua = input('Deseja continuar? [s/n] ').strip().lower()
    while continua not in ['s', 'n']:
        print('Opção inválida! Digite "s" para sim ou "n" para não.')
        continua = input('Deseja continuar? [s/n] ').strip().lower()

    if continua == 'n':
        break

# Saída de dados
print('-=' * 20)
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":>8}')
print('-' * 30)
for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<15}{aluno[3]:>8.2f}')