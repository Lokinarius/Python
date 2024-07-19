# Exemplo 1:
for c in range(10, 0, -1):
    # (Inicio,Fim,iteração)
    print(c)
print('Fim')

# Exemplo 2:
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim')

# Exemplo 3:
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

# Exemplo 4:
s = 0
for c in range(0, 4):
    num = int(input('digite um valor: '))
    s += num
    print(f'O somatório de todos os valores foi {s}')
