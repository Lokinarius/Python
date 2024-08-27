# DICIONARIOS

# Dicionários em Python são identificados pelo uso de chaves " {} "
dados = dict()
# Utiliza-se o comando dict() para criação de um dicionário
dados = {'nome': 'Will', 'idade': 28}
# Adicionando elementos ao dicionário
dados['sexo'] = 'M'
dados['peso'] = 80.9
# Removendo elementos do dicionário
del dados['idade']
print(dados)

# Outra maneira de criar um dicionário
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas',
    'elenco': ['Luke Skywalker','Leia Organa','Han Solo','Chewbacca']
}
# Para pegar os valores se utiliza o comando '.values()'
print(filme.values())
# Para pegar as chaves utiliza o comando '.keys()'
print(filme.keys())
# Exemplo de loop
for chave, valor in filme.items():
    print(f'{chave}: {valor}')

# Misturando dicionários com listas
pessoas = [
    {'nome': 'Will', 'idade': 28, 'sexo': 'M'},
    {'nome': 'Alice', 'idade': 25, 'sexo': 'F'},
    {'nome': 'Roberto', 'idade': 30, 'sexo': 'M'},
    {'nome': 'Eve', 'idade': 27, 'sexo': 'F'},
    {'nome': 'Carolina', 'idade': 26, 'sexo': 'F'},
    {'nome': 'Daniel', 'idade': 29, 'sexo': 'M'},
]
pronome = ''
while len(pessoas):
    pessoa = pessoas.pop(0)
    if pessoa['sexo'] == 'M':
        pessoa['sexo'] = 'masculino'
        pronome = 'O'
    elif pessoa['sexo'] == 'F':
        pessoa['sexo'] = 'feminino'
        pronome = 'A'
    print(f'{pronome} {pessoa["nome"]} que tem {pessoa["idade"]} é do sexo {pessoa["sexo"]}')
