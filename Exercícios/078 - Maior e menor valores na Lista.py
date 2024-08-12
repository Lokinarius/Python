# Cabeçalho
print('\t\tMAIOR E MENOR VALORES NA LISTA')
print('-' * 20)

# variaveis
lista = []
maior = 0
menor = 0

# Entrada de dados
for i in range (5):
    valor = int(input(f'Digite o {i}ª valor : '))
    lista.append(valor) # adiociona valor a cada elemento da lista
    if i == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

# Saída de daddos
print('-=' * 10)
print(f'Você digitou os valores {lista}')
# Posições para maior e menor
maior_posicoes = [i for i, x in enumerate(lista) if x == maior]
menor_posicoes = [i for i, x in enumerate(lista) if x == menor]
print(f'O maior valor digitado foi {maior}, e se encontra nas posições {maior_posicoes}')
print(f'O menor valor digitado foi {menor}, e se encontra nas posições {menor_posicoes}')
