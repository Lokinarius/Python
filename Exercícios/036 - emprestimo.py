print('Aprovação de Empréstimo bancário')
print('--------------------------------')
print('\n')
# Entrada dos dados do solicitante
nome = str(input('Nome: '))
salario = float(input('Renda mensal do solicitante: '))
casa = float(input('Valor da casa a ser comprada com o empréstimo: '))
anos = int(input('em quantos anos a casa será paga: '))
prestacao = (anos * 12) / casa

# Condições de aprovação
aprovado = (salario * 0.3)
if aprovado >= prestacao:
    print(f'{nome}, você está apto para realizar o empréstimo.')
    print(f'A prestação será de R${prestacao:.2f} por mês.')
else:
    print(f'{nome} infelizmente não atende os requisitos para realizar tal empréstimo.')

