# OPERADORES ARITIMÉTICOS

# +  Adição
# -  Subtração
# *  Multiplicação
# /  Divisão
# ** Potênciação -->> **(1/2) Raiz quadrada
# // Divisão inteira
# %  Resto da divisão


# ORDEM DE PRECEDÊNCIA

# 1 { () }
# 2 { ** }
# 3 { * / // % }
# 4 { + - }

# Operadores funcionam inclusive com strings e caracters
# >>> print('='*20)
# ====================

nome = input('qual é o seu nome? ')
print(f'Prazer em te conhecer, {nome}!')
# :< Alinhado a esquerda
print(f'Prazer em te conhecer, {nome:<10}!')
# :> Alinhado a direita
print(f'Prazer em te conhecer, {nome:>10}!')
# :^ Centralizado
print(f'Prazer em te conhecer, {nome:^10}!')
# Caso seja colocado um caracter na fórmula, o caracter fica no espaço selecionado
print(f'Prazer em te conhecer, {nome:=^12}!')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s},o produto é {m} e a divisão{d}')
print(f'Divisão inteira {di} e potência{e}')
