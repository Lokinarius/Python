# Cabeçalho
print('================================')
print('\t\tVALORES')
print('================================')

# Variavés
soma = 0
n = 0
media = 0

# Entrada de dados
while True:
    num = int(input('Digite um número: '))
    soma += num
    n += 1
    if n == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    while True:
        continuar = str(input('Deseja continuar? ')).strip().upper()
        if continuar in ('S', 'N'):
            break
        else:
            print('Opção inválida! Informe "S" para sim ou "N" para não.')
    if continuar == 'N':
        break

# Resultado final
media = soma / n
print('Resultados: ')
print(f'Foram digitado um total de {n} valores, a soma entre esse valores é de {soma}, e a média é de {media}.')
print(f'O maior valor digitado foi {maior} e o menor valor digitado foi {menor}.')
