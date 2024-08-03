# Cabeçalho
print('\t\tTABUADA 3.0')

# Entrada de dados
while True:
    print('================================\n')
    num = int(input('Digite um número: '))
    if num <= 0:
        if num == 0:
            print('O Número 0 foi digitado, o programa será encerrado...')
        else:
            print('Um Número negativo foi digitado, o programa será encerrado...')
        break
    else:
        for n in range(1, 11):
            mult = num * n
            print(f'{num} X {n} = {mult}')
