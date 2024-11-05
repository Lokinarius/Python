
# CABEÇALHO
print("Função que calcula área")
print(30 * "-")


# FUNÇÃO AREA
def area(largura, comprimento):
    resultado = largura * comprimento
    print(f'A Area de um terreno {largura} X {comprimento} é de {resultado} m²')
    return resultado


# ENTRADA DE DADOS
largura = float(input('Informe a largura do terreno em m²: '))
comprimento = float(input('Informe o comprimento do terreno em m²: '))

# CALCULO DA AREA
area(largura, comprimento)
