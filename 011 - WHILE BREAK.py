# Modelo sem loop infinito
c1 = 1
while c1 <= 10:
    print(c1, '->', end='')
    c1 += 1
print('Fim')
print('--------------------------------\n')

# Modelo com loop infinito interrompido com break
c2 = 1
while True:
    print(c2, '->', end='')
    if c2 == 10:
        break
    c2 += 1
print('Fim')
print('--------------------------------\n')
