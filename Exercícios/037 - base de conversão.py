print('BASE DE CONVERSÃO')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
decimal = int(input('insira o número na base decimal para para converte-lo: '))
binario = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)
print('Para qual base deseja converte-lo?')
escolha = int(input('[1]Binarário\n[2]Octal\n[3]Hexadecimal\n'))
if escolha == 1:
    print('--------------------------------')
    print(f'{decimal} em binário é {binario[2:]}')
elif escolha == 2:
    print('--------------------------------')
    print(f'{decimal} em octal é {octal[2:]}')
elif escolha == 3:
    print('--------------------------------')
    print(f'{decimal} em hexadecimal é {hexadecimal[2:]}')
else:
    print('--------------------------------')
    print('Opção inválida.')
