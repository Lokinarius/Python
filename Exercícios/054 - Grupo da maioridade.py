from datetime import datetime
# Cabaçalho
print('\t\tGRUPO DA MAIORIDADE')
print('--------------------------------')

# Declaração de variáveis
maior_idade = 0
menor_idade = 0
ano = datetime.now().year

# Entrada de dados
for c in range(1,8):
    nasc = int(input(f'Em que ano o {c}º integrante nasceu? '))
    idade = ano - nasc
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

# Resultado
print('--------------------------------')
print(f'No grupo {maior_idade} pessoas são maiores de idade, e {menor_idade} pessoas são menores de idade.')

