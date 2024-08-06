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
print('Times classificados para libertadores: ')
print(times[0:6])
print('Times na zona de Rebaixamento: ')
print(tuple(reversed(times[-4:]))) # times([17:21])
print('Times em ordem alfabética')
print(sorted(times))
