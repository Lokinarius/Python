dist = int(input('Qual a distância da viagem em km? '))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('--------------------------------\n')
print(f'Em uma viagem de {dist}km, o valor da viagem custa R${preco:.2f}')
