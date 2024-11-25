import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.cambio(p)} é {moeda.cambio(moeda.metade(p))}')
print(f'O dobro de {moeda.cambio(p)} é {moeda.cambio(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.cambio(p)} temos {moeda.cambio(moeda.aumentar(p, 10))}')
print(f'Reduzindo 15% de {moeda.cambio(p)} temos {moeda.cambio(moeda.diminuir(p, 15))}')