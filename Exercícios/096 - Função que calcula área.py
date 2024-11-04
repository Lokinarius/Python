"""
096
Faça um programa que tenha uma função chamada de área(),
que receba as dimensões de um terreno retangular
e mostre a área do terreno
"""

# CABEÇALHO
print("Função que calcula área")
print(30 * "-")

# FUNÇÃO AREA
def area(largura, comprimento):
    return largura * comprimento

# ENTRADA DE DADOS
largura = float(input("Informe a largura do terreno: "))
comprimento = float(input("Informe o comprimento do terreno: "))

# CALCULO DA AREA
print("A área do terreno é de " + str(area(largura, comprimento)))
