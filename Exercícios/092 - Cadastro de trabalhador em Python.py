"""
092
# Se a clt for dirente de zero ela para
# Calculo da idade
# idade da aposentadoria considerando 40 anos de contribuição
"""
# Bibliotecas
from datetime import datetime

# Cabeçalho
print('\t\tCadastro de trabalhador')
print('---------------------------------')

# Entrada de dados
trabalhador = {
    'nome': str(input('Nome: ')),
    'nascimento': int(input('Ano de nascimento: ')),
    'idade': datetime.now().year - int(input('Ana de nascimento: ')),
    'clt': input('CLT: '),
    'contratação': int(input('Ano de contratação: ')),
}

# Se a clt for dirente de zero, para o calculo da idade e da aposentadoria
if int(trabalhador['clt']) > 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - datetime.now().year)

# Saida de dados
print('-='*20)
for k, v in trabalhador.items():
    print(f'{k}: {v}')
