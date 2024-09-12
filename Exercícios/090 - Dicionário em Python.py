# Cabeçalho
print('\t\tDICIONÁRIO EM PYTHON')
print('---------------------------------')

# entrada de dados
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno['nome']}'))
if aluno['media'] >= 7:
    aluno['situacão'] = 'Aprovado'
elif 4 <= aluno['media'] < 7:
    aluno['situacão'] = 'Recuperação'
else:
    aluno['situacão'] = 'Reprovado'

# saida de dados
for k, v in aluno.items():
    print(f'{k}: {v}')
