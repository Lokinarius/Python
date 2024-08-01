# Cabeçalho
print('================================')
print('\t\tNÚMERO COM FLAG')
print('================================\n')

# Variáveis
soma = 0
n = 0

# Entrada de dados
print('DIGITE VÁRIOS NÚMEROS E VEJA SUA SOMA FINAL')
print('Digite 999 para parar')
while True:
    num = int(input('Digite um número: '))
    n += 1
    if num == 999:
        break
    if num != 999:
        soma += num
print(f'Foram digitados {n} números, e a soma final foi de {soma}')
