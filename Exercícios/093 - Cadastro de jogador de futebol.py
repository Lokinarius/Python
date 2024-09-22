"""
093
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidades de gols feitos em cada partida.
No final final tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""
# CABEÇALHO
print("Cadastro de Jogador de Futebol")
print("-="*30)



# ENTRADA DE DADOS
jogador = {
    "nome": input("Nome do jogador: ").capitalize(),
    "partidas" : int(input("Quantas partidas ele Jogou: ")),
    "gols": []
}
# Adiciona gols feitos por partida
for i in range(jogador["partidas"]):
    gol = int(input(f"Quantos gols na partida {i+1}: "))
    jogador["gols"].append(gol)

# SAÍDA DE DADOS
print("-="*30)
for k, v in jogador.items():
    print(f"{k.capitalize()}: {v}")
