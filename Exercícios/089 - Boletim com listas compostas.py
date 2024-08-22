# Cabeçalho
print('\t\tBOLETIM DE NOTAS')
print('-------------------------------------')

# Variaveis
aluno = list()
alunos = list()
alunos.append(aluno[:])

# Entrada de dados
while True:
    print('\n================================')
    nome = (str(input('Nome do aluno: ')))
    alunos.append(nome)
    n1 = float(input(f'1ª nota: '))
    while True:
        if not n1 > 0 and n1 <= 10:
            print(' nota inválida! Digite uma Nota entre 0 e 10')
        else:
            aluno.append(n1)
            break
    n2 = float(input(f'2ª nota: '))
    while True:
        if not n2 > 0 and n2 <= 10:
            print('Nota inválida! Digite uma Nota entre 0 e 10')
        else:
            aluno.append(n2)
            break
    media = (n1 + n2)/2
    aluno.append(media)
    continua = str(input('Deseja continuar? [s/n]')).strip().upper()
    while continua not in ['S', 'N']:
        print('Opção inválida! Digite "S" para sim ou "N" para não')
        continua = str(input('Deseja continuar? [s/n]')).strip().upper()
        if continua == 'N':
            break

# Saída de dados
print('-=-=-=-=-=-=-=-=-' * 3)
print('no. NOME\t\t MÉDIA')
print('----------------'* 2)
for i in range(1, len(alunos)):
    print(f'{i-1}\t{alunos[i]}\t\t{alunos[i+1]}')
