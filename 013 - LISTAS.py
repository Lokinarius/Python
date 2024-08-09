# Listas
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('Nas listas o valor de um elemento é mutável')
num[3] = 10
print(num)
# a saída será [0, 1, 2, 10, 4, 5, 6, 7, 8, 9]
print('-' * 15)

print('.insert insere um valor')
print('num.insert(2, 5)')
num.insert(2, 5)
print(num)
print('-' * 15)

print('Para remover um elemento utilizamos .pop')
num.pop(5)
print(num)
print('-' * 15)


print('Para remover um elemento específico utilizamos o .remove')
print('num.remove(10)')
num.remove(10)
print(num)
print('-' * 15)


print('utilizar o .sort ele coloca de maneira ordenada e o (reverse=True) o coloca de maneira invertida')
print('num.sort(reverse=True)')
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
print('-' * 15)



print('Para adicionar um elemento utilizamos .append')
print('num.append(5)')
print('num.append(10)')
print('num.append(15)')
valores = []
valores.append(5)
valores.append(10)
valores.append(15)
print('-' * 15)

print('O elemento .enumerate serve para indicar o valor que está naquela posição')
print('for c, v in enumerate(valores):')
print('\tNa posição {c} encontrei o valor {v}')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')
print('-' * 15)

print('Também é possivel adicionar valores na lista através do input:')
print('valores = list()')
print('for cont in range (0,5):')
print('\tvalores.append(int(input(\'Digite um valor: \')))')
valores = list()
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))

print('nas listaS existe uma diferença entre ligação e copia')
print('a = [1, 2, 3, 4]')
print('b = a')
print('b[2] = 8')
print('A saída das lista será:')
print('Lista A: [1, 2, 3, 4]')
print('Lista B: [1, 2, 3, 4]')
print('Mas caso seja utilzado o comando')
print('b = a[:]')
print('A saída das listas será:')
print('Lista A: [1, 2, 3, 4]')
print('Lista B: [1, 2, 8, 4]')


