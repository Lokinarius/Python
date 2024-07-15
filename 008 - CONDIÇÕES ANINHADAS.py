nome = str(input('Quem está acessando o computador?  '))
if nome == 'William':
    print(f'Olá, {nome}, seja bem vindo!')
    sen = 'Programa Dor'
    senha = str(input('insira a senha: '))
    if senha == sen:
        print(f'Olá, {nome}, seja bem vindo!')
    else:
        print('Senha incorreta!')
elif nome == 'Convidado':
    print('Você é um convidado, não possui permissão plena sobre o conteúdo.')
else:
    print('Você não tem permissão para acessar este computador.')
