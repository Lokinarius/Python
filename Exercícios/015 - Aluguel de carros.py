dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
valor = (60 * dias) + (km * 0.15)
print(f'O total a pagar é de R${valor:.2f}')