from time import sleep
# CABEÇALHO
print("================================")
print("Contador de valores...")
print("================================")

# FUNÇÃO DE CONTAGEM
def contador(inicio,fim,passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for i in range(inicio,fim + 1, passo):
            print(f'{i}',end =' ')
            sleep(0.5)

    else:
        for i in range(inicio, fim - 1, -passo):
            print(f'{i}',end =' ')
            sleep(0.5)
    print("================================")

# SAIDA DE DADOS
print("Contagem 1: ")
contador(1, 10, 1)

print("\nContagem 2: ")
contador(10, 0, -2)

print("\nContagem personalizada:")
inicio = int(input("Qual será o início da contagem? "))
fim = int(input("Qual será o fim da contagem? "))
passo = int(input("Qual será o passo da contagem? "))
contador(int(inicio), int(fim), int(passo))
