# [ Forma import]
# import moeda


# [Forma from import]
import moeda

p = float(input('Digite o preço: R$'))
# [ Forma import]
# print(f'A metade de R${p} é {moeda.metade(p)}')
# print(f'O dobro de R${p} é {moeda.dobro(p)}')
# print(f'Aumentando 10% de R${p} temos R${moeda.aumentar(p, 10)}')
# print(f'Reduzindo 15% de R${p} temos R${moeda.diminuir(p, 15)}')

# [Forma from import]
print(f'A metade de {moeda.cambio(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.cambio(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10% de {moeda.cambio(p)} temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 15% de {moeda.cambio(p)} temos {moeda.diminuir(p, 15)}')
