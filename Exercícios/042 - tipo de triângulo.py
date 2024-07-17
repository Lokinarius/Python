print('\tTIPOS DE TRIÃNGULO')
print('=-=-=-=-=-=-=-=-=-=-=-=-=')
a = float(input('Informe o tamanho do primeiro lado: '))
b = float(input('Informe o tamanho do segundo lado: '))
c = float(input('Informe o tamanho do terceiro lado: '))

# Verificando se os lados formam um triângulo
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print('Os lados formam um triângulo equilátero.')
    elif a != b and a != c and b != c:
        print('Os lados formam um triângulo escaleno.')
    else:
        print('Os lados formam um triângulo isósceles.')
else:
    print('Os lados não formam um triângulo.')
