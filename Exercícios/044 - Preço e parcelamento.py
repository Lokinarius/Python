print('CALCULE O PREÇO DO PRODUTO')
print('-----------------------------')
preco = float(input('Qual é o preço normal do produto? R$'))

# Calculos
vista_din = preco - (preco * 0.1)
vista_car = preco - (preco * 0.05)
parcela_3 = preco + (preco * 0.2)

# condições de pagamento
pagamento = int(input('Como pretende pagar o produto?\n[1]Á vista\n[2]Á vista no cartão\n[3]Parcelado em 2x\n['
                      '4]Parcelado em 3x ou mais'))
match pagamento:
    case 1:
        print('--------------------------------')
        print(f'Pagamento á vista em dinheiro com 10% de desconto. O preço final é R${vista_din}')
    case 2:
        print('--------------------------------')
        print(f'Pagamento á vista no cartão com 5% de desconto. O preço final é R${vista_car}')
    case 3:
        print('--------------------------------')
        print(f'Parcelado em 2x. O preço final é R${preco}')
    case 4:
        print('--------------------------------')
        print(f'Parcelado em 3x ou mais. O preço final é R${parcela_3}')
    case _:
        print('--------------------------------')
        print('Opção de pagamento inválida.')
