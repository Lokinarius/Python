"""
094
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo.
c) Uma lista com todas as mulheres.
d) uma lista com todas as pessoas com idade acima da média.
"""
# [CABEÇALHO]
print("================================")
print("Cadastrando pessoas...")
print("================================")

# [LISTAS]
pessoas_cadastradas = 0
mulheres = []
idades = 0
idade_media = 0
pessoas_mais_idade_media = []

# [ENTRADA DE DADOS]
# Cadastro de pessoas
while True:
    pessoas = {
        "nome": input("Nome: ").capitalize(),
        "sexo": input("Sexo (M/F): ").upper(),
        "idade": int(input("Idade: "))
    }

    # [CRIANDO LISTAS]
    # Pessoas cadastradas
    pessoas_cadastradas += 1
    # Média de idade
    idades += pessoas["idade"]
    idade_media = idades / pessoas_cadastradas

    # Listas
    if pessoas["sexo"] == "F":
        mulheres.append(pessoas["nome"])
    if pessoas["idade"] > idade_media:
        pessoas_mais_idade_media.append(pessoas["nome"])

    # Verificação de saída do loop
    while True:
        continua = input("Deseja continuar? (N/S)").lower()
        if continua != "n" and continua != "s":
            print("Opção inválida! Aperte N para sair, ou S para continuar!")
        else:
            break
    if continua == "n":
            break

# [SAIDA DE DADOS]
print("==================================")
print(f"Quantidade de pessoas cadastradas: {pessoas_cadastradas}")
print(f"Média de idade do grupo: {idade_media:.2f} anos")
print("Mulheres cadastradas:")
for mulher in mulheres:
    print(mulher)
if pessoas_mais_idade_media:
    print("Pessoas com idade acima da média:")
    for pessoa in pessoas_mais_idade_media:
        print(pessoa)
else:
    print("Nenhuma pessoa tem idade acima da média.")









