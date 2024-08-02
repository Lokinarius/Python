# Cabeçalho
print('\t\tANÁLISE DE DADOS')
print('---------------------------------')

# Variaveis
n = 0
homem = 0
mulher_20 = 0
maior = 0

# Entrada de dados
while True:
    print('\n================================')
    n += 1

    # Idade
    idade = int(input(f'Informe a idade da {n}ª pessoa: '))
    if idade < 0:
        print('Idade inválida! Informe um número positivo.')
        continue
    else:
        if idade >= 18:
            maior += 1

    # Sexo
    sexo = input(f'Informe o sexo da {n}ª pessoa: ').strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo inválido! Informe M para masculino ou F para feminino.')
        continue
    elif sexo == 'M':
        homem += 1
    elif sexo == 'F':
        if idade <= 20:
            mulher_20 += 1

    # Continuar
    cont = input('Deseja continuar? ').strip().upper()
    if cont not in ['S', 'N']:
        print('Opção inválida! Informe "S" para sim ou "N" para não')
        continue
    elif cont == 'N':
        break

# Resultados
print('\nResultados:')
print(f'Foram cadastradas {n} pessoas.')
if maior > 0:
    print(f'Existem {maior} pessoas maiores de idade.')
if homem > 0:
    print(f'Há {homem} homens.')
if mulher_20 > 0:
    print(f'Existem {mulher_20} mulheres com 20 anos ou mais.')