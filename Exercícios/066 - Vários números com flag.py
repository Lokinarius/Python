# Cabeçalho
print('================================')
print('\t\tNÚMERO COM FLAG')
print('================================\n')

# Variáveis
soma = 0
n = 0

# Entrada de dados
print('DIGITE VÁRIOS NÚMEROS E VEJA SUA SOMA FINAL')
print('Digite um número acima de 999 para parar')
while True:
    num = int(input('Digite um número: '))
    if num >= 999:
        break
    if num <= 999:
        n += 1
        soma += num
print(f'Foram digitados {n} números, e a soma final foi de {soma}')
