preco = float(input('Qual o é o preço do produto: R$'))
desconto = 5 * (preco / 100)
valor = preco - desconto
print(f'O produto custava R${preco}, na promoção com desconto de 5%, ele vai custar R${valor:.2f}')