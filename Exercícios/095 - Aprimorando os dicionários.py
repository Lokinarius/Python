"""
095
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

# CABEÇALHO
print("Cadastro de Jogador de Futebol")
print("-="*30)

# ENTRADA DE DADOS
while True:
    jogador = {
        "nome": input("Nome do jogador: ").capitalize(),
        "partidas" : int(input("Quantas partidas ele Jogou: ")),
        "gols": []
    }
    # Adiciona gols feitos por partida
    for i in range(jogador["partidas"]):
        gol = int(input(f"Quantos gols na partida {i+1}: "))
        jogador["gols"].append(gol)

    # Verificação de saída do loop
    while True:
        continua = input("Deseja continuar? (N/S)").lower()
        if continua != "n" and continua != "s":
            print("Opção inválida! Aperte N para sair, ou S para continuar!")
        else:
            break
    if continua == "n":
            break

# SAÍDA DE DADOS
print('=*'*20)
print(f"{'Nome':<10}{'Partidas':<10}{'Gols':<10}{'Média':<10}")
print('=*'*20)
for k, v in jogador.items():
    print(f"{v:<10}{jogador['gols'].count(v):<10}{sum(jogador['gols']):<10}{sum(jogador['gols'])/len(jogador['gols']):<10.2f}")
