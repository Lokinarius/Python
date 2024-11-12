
# CABEÇALHO
print("[FUNÇÃO FATORIAL]")
print(15*"=")

# FUNÇÃO FATORIAL
def fatorial():
    numero = int(input('Digite um número: '))
    if numero < 0 or numero == 0:
        print('Número inválido!')
        return
    else:
        fat = 1
        for c in range(1, numero +1):
            fat *= c
    print(f'O número fatorial de {numero} é {fat}')

# Saída
fatorial()
