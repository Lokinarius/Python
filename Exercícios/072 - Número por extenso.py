# Cabeçalho
print('\t\tNÚMERO POR EXTENSO')
print('--------------------------------')

# Entrada de dados
num = int(input('Digite um número entre 0 e 20: '))

# Converte o número para extenso
extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
    "dezoito", "dezenove", "vinte"
)

# Saída de dados
while True:
    if 0 <= num <= 20:
        print(f'Você digitou o número {extenso[num]}')
        break
    else:
        num = int(input('Número inválido. Digite um número entre 0 e 20: '))