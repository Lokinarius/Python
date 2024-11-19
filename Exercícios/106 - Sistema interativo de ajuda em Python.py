"""
106
Faça um mini-sistema que utiliza o interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
"""
# Lista de cores
c = ('\033[m', # 0 - sem cores)
    '\033[0;30m', # 1 - preto
    '\033[0;31m', # 2 - vermelho
    '\033[0;32m', # 3 - verde
    '\033[0;33m', # 4 - amarelo
    '\033[0;34m', # 5 - azul
     )
# Função
def ajuda(comando):
    """
    Função para mostrar o manual do Python.
    """
    titulo(f'Acessando o manual do comando \'{comando}\'',5)
    help(comando)

def titulo(msg, cor = 0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('=' * tamanho)
    print(msg)
    print('=' * tamanho)
    print(c[0], end='')

# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP',4)
    comando =str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        print(f"Manual do Python: help({comando})")
titulo('ATÉ LOGO',2)