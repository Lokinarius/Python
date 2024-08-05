# TUPLAS

# Estrutura Simples
lanche1 = 'Hamburguer'
# Estrutura Composta
lanche2 = ('Hamburguer', 'Pizza', 'Batata Frita')
# Elemento
print(lanche2[0]) # Hamburguer
print(lanche2[1]) # Pizza
print(lanche2[2]) # Batata Frita
for comida in lanche2:
    print(f'Eu vou comer {comida}')

for c in range(0, len(lanche2)):
    print(f'A {c}ª coisa que vou comer vai ser {lanche2[c]}')

print(sorted(lanche2)) # para a tupla colocar em ordem alfabética

# Tuplas são imutáveis, não podem ser alteradas
# Caso haja uma alteração como : lanche2[0] = 'Café'
# haverá um erro no programa

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) # Concatena as tuplas
print(len(c)) # Mede o número de elementos
print(c.count(5)) # Conta qquantas vezes dceterminado elemento aparece na tupla
print(c.index(8)) # Mostra a ocorrência do elemento na tupla

# Diferente de vetores a tupla aceita tipos diferentes de variáveis
pessoa = ('William', 28, 'M', 78.9)
print(pessoa)
