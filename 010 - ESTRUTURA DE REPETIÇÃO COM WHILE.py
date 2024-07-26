# O For usualmente é utilizado para situações onde sabe-se o limite da repetição
'''
for c in range(1,10)
        print(c)
    print('Fim')
'''

# O While pode ser utilizado quando não se sabe o limite

# Exemplo 1
num = 1
while num != 0:
    num = int(input('Digite um número: '))
print('Fim')

# Exemplo 2
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? ')).upper()
print('Fim')

# Exemplo 3
number = 1
even = 0
odd = 0
while number != 0:
    number = int(input('Digite um número: '))
    if number != 0:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
print(f'Você digitou {even} números pares, e {odd} números ímpares.')
