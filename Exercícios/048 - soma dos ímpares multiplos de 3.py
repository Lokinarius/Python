print('\t\tSOMA DOS ÍMPARES MÚLTIPLOS DE 3')
print('----------------------------------------------------------------')
s = 0
c = 0
for n in range(1,500):
    if n % 3 == 0 and n % 2 != 0:
        s += n
        c += 1
        print(f'{n}')
        print('+')
print(f'Entre 1 e 500 existem {c} valores, e a soma de todos ímpares é  de {s}')


