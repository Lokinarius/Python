# Listas
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Nas listas o valor de um elemento é mutável
num[3] = 10
print(num)
# a saída será [0, 1, 2, 10, 4, 5, 6, 7, 8, 9]

# Para adicionar um elemento utilizamos .append
num.append(11)
print(num)

# .insert insere um valor
num.insert(2, 5)
print(num)

# Para remover um elemento utilizamos .pop
num.pop(5)
print(num)

# Para remover um elemento específico utilizamos o .remove
num.remove(10)
print(num)

# utilizar o .sort ele coloca de maneira ordenada e o (reverse=True
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
