print('\t\tSOMA DOS ÍMPARES MULTIPLOS DE 3')
print('----------------------------------------------------------------')
s = 0
for n in range(1,500):
    if n % 3 == 0 and n % 2 != 0:
        s += n
        print(f'{n}')
        print('+')
print(f'= {s}')

