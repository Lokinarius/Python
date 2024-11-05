

def msg(mensagem):
    tamanho = len(mensagem) + 4
    print('~*' * (tamanho // 2))
    print(f' {mensagem} ')
    print('~*' * (tamanho // 2))


# ENTRADA
mensagem = input('Digite uma mensagem aqui: ')

# SAIDA
msg(mensagem)
