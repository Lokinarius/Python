# Cabeçalho
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\t\tCALCULADORA')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

while True:
    # Entrada de dados
    operacao = input('\nInforme a operação:\n[1]Somar\n[2]Multiplicar\n[3]Subtrair\n[4]Dividir\n[5]Sair do '
                     'programa\n')
    num1 = int(input('Informe o primeiro valor: '))
    num2 = int(input('Informe o segundo valor: '))

    # Condições para as operações
    if operacao == '1':
        res = num1 + num2
        print(f'A soma entre {num1} e {num2} é {res}')
    elif operacao == '2':
        res = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} é {res}')
    elif operacao == '3':
        res = num1 - num2
        print(f'A subtração entre {num1} e {num2} é {res}')
    elif operacao == '4':
        if num1 or num2 == 0:
            print('Não é possível realizar uma divisão por zero.')
        else:
            res = num1 / num2
            print(f'A divisão entre {num1} e {num2} é {res}')
    elif operacao == '5':
        print('Saindo do programa...')
        break
    else:
        print('Operação inválida! Tente novamente.')
        operacao = input('Informe a operação:\n[1]Somar\n[2]Multiplicar\n[3]Subtrair\n[4]Dividir\n[5]Sair do programa\n')