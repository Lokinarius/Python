from datetime import date
# Cabeçalho
print('\tALISTAMENTO OBRIGATORIO')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# Dados do jovem
nome = str(input('Qual o seu nome? '))
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
falta = 18 - idade
passou = idade - 18

# verificação
if idade < 18:
    print(f'{nome}, você ainda tem {idade} anos, ainda faltam {falta} anos para que você possa se alistar!')
elif idade > 18:
    print(f'{nome}, você já possui {idade} anos, espero que já tenha servido, ou você está a {passou} anos em dívida '
          f'com o '
          f'serviço militar obrigatório!')
else:
    print(f'{nome}, você possui {idade}, dirija-se para o posto militar mais próximo para que possar se alistar!')