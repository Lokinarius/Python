import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentando 10% de R${p} temos R${moeda.aumentar(p, 10)}')
print(f'Reduzindo 15% de R${p} temos R${moeda.diminuir(p, 15)}')
