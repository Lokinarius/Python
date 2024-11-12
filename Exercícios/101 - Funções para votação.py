
from datetime import datetime

# Cabeçalho
print("[URNA ELETRONICA]")
print("=========================")

# Função voto()
def voto():
    # Calculo de idade
    ano_nascimento = int(input("Em que ano você nasceu? "))
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    # Verificação de idade
    if idade < 16:
        return f"Você tem {idade} anos, você ainda não pode votar."
    elif 18 <= idade <= 65:
        return f"Você tem {idade} anos, seu voto é obrigatório."
    else:
        return f"Você tem {idade} anos, seu voto é opcional."

# Saída
print(voto())



