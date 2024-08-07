# cabeçalho
print('\t\tTIMES DE FUTEBOL')
print('-------------------------------------')

# declarações de variáveis
times = (
    "Botafogo", "Flamengo", "Fortaleza", "Palmeiras", "Cruzeiro", "São Paulo",
    "Bahia", "Athletico-PR", "Atlético-MG", "Red Bull Bragantino", "Vasco",
    "Criciúma", "Juventude", "Internacional", "Fluminense", "Grêmio",
    "Corinthians", "Santos", "Goiás", "Coritiba"
)

# Saída de dados
print(f'Times classificados para libertadores:\n {times[0:6]}')
print(f'Times na zona de Rebaixamento:\n {times[-4:]} ')
print(f'Times em ordem alfabética:\n {sorted(times)}')
