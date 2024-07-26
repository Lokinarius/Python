# Cabeçalho
print('\tCALCULO FATORIAL')

# Entrada de dados
while True:
    print('\n================================')
    print('Informe um número para ver o sua fatorial\nDigite 0 para sair do programa')
    num = int(input(''))
    if num < 0:
        print('Número invalido! Informe um número positivo!')
    elif num == 0:
        print('Program encerrado')
        break
    else:
        fat = 1
        for n in range(1, num + 1):
            fat *= n
            print(f'{n}! = {fat}')
