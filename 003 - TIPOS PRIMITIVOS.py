# [ TIPOS PRIMITIVOS ]

# NÚMEROS INTEIROS
# [ int = 7, -4 , 0 , 9875 ]
# NÚMEROS REAIS OU PONTO FLUTUANTE
# [ float = 4.5, 0.078, -15.223, 7.0 ]
# LÓGICO OU BOLEANO
# [ bool = true, false ]
# STRING
# [ str = 'Olá', 'Maria', '7.5', '' ]

# É importante definir o tipo primitivo dentro da variável

# Exemplo 1
n1 = (input('Digite um valor: '))
n2 = (input('Digite outro valor: '))
s1 = n1 + n2
print('A soma dos valores foi concatenada no valor ' + s1 + ' :p')

# Exemplo 2
# A insersão do tipo primitivo é importante para o funcionamento correto do código
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite outro valor: '))
s2 = n3 + n4
print('A soma entre {0} e {1} vale {2}' .format(n3, n4, s2))