# Função
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
            break
        else:
            print('ERRO! Por favor, digite um número válido.')
        if ok:
            break
    return valor

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
