# Cabeçalho
print('\t\tANALISADOR COMPLETO')
print('---------------------------------')

# Variaveis
soma_idade = 0
media_idade = 0
homem_velho = 0
homem_velho_nome = ''
mulher_20 = 0

# Entrada de dados
for c in range(1,5):
    nome = str(input(f'Nome da {c}ª pessoa: '))
    idade = int(input(f'Idade da {c}ª pessoa: '))
    soma_idade += idade
    sexo = input(f'Sexo da {c}ª pessoa(M/F): ').upper()
    if sexo == 'm':
        if c == 1:
            homem_velho = idade
            if homem_velho > idade:
                homem_velho_nome = nome
    elif sexo == 'f':
        if idade < 20:
            mulher_20 += 1

media_idade = soma_idade/4

#Resultados
print('---------------------------------')
print(f'A média de idade do grupo é {media_idade}')
print(f'O nome do homem mais velho é {homem_velho_nome}')
print(f'Existem {mulher_20} abaixo dos 20 anos')

