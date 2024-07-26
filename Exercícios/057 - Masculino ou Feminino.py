# Cabeçalho
print('\t\tMASCULINO OU FEMININO')
print('-------------------------------------')

# DECLARAÇÃO DE VARIÁVEIS


# ENTRADA DE DADOS
while True:
    sexo = str(input('Qual o sexo da pessoa? (M/F): ')).strip().upper()
    if sexo == 'M':
        print('Pessoa do sexo masculino.')
        break
    elif sexo == 'F':
        print('Pessoa do sexo feminino.')
        break
    else:
        print('Sexo inválido. Tente novamente.')
