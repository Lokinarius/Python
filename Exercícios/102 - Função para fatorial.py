
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
        fat =1
        print(f'Cálculo do fatorial de {numero}: ', end='')
        for c in range(1, numero + 1):
            fat *= c
            if c == numero:
                print(c, end=' = ')
            else:
                print(c, end=' x ')
        print(fat)

# Saída
fatorial()
