# CABEÇALHO
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\t\tPROGRESSÃO ARITMÉTICA')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

# ENTRADA DE DADOS
a1 = float(input('Informe o primeiro termo da progressão aritmética: '))
r = float(input('Informe a razão da progressão aritmética: '))
n = int(input('Informe o número de termos: '))

# CÁLCULO DO ÚLTIMO TERMO
an = a1 + (n - 1) * r

# EXIBIÇÃO DOS TERMOS
print('\nOs termos da progressão aritmética são: ')
for i in range(n):
    termo = a1 + i * r
    print(f'Termo {i+1}: {termo}')
