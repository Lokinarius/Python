frase = 'Curso em Vídeo Python'

# [ C][ u][ r][ s][ o][  ][ e][ m][  ][ V][ í][ d][ e][ o][  ][ P][ y][ t][ h][ o][ n]
# [ 0][ 1][ 2][ 3][ 4][ 5][ 6][ 7][ 8][ 9][10][11][12][13][14][15][16][17][18][19][20]


# {REGRAS DE FATIAMENTO DE STRING}


# frase[9] = 'V'
# frase[9:13] = 'Vide'
# O primeiro número é o ponto de partida
# O último valor não entra na contagem

# frase[9:21:2] = 'VdoPto'
# O terceiro elemento serve para pular valores

# frase[:5] = 'Curso'
# iniciando com o ':',O vai do inicio da lista até o valor indicado

# frase[15:] = 'Python'
# finanlizando com ':', sem indicar um valor, a lista vai até o final

# frase[9::3] = 'VePh'
# Vai até o final pulando casas no terceiro elemento


# {ANALISE DE STRINGS}


# length
# len(frase)
# analisa o comprimento da string

# frase.count()
# conta quantas vezes existem determinado carácter
# Exemplo:
# frase.count('o',0,13) = 1

# frase.find('deo')
# frase.find('deo') = 11
# encontra a posição a onde encontra o caracter
# caso não exista a string, ele retorna -1

# 'Curso' in frase
# true
# Retorna um booleano

# frase.replace('Python','Android')
# substitui os caracters da string
# frase = 'Curso em Video Android'

# frase.upper()
# Transforma a string em maiúsculo
# frase = 'CURSO EM VIDEO PYTHON'

# frase.lower()
# Transforma a string em minúsculo
# frase = 'curso em vídeo python'

# frase.capitalize()
# transforma a preimeira letra em Maiúscula e todo resto em minúscula
# frase = 'Curso em vídeo python'

# frase.title()
# Mesma função do capitalize, mas palavra por palavra
# frase = 'Curso Em Vídeo Python'


# {TRASFORMAÇÃO DE STRINGS}

# frase.strip()
# remove espaços do ínicio e final
# adiocinando 'r' ou 'l', é possível remover espaços somente da direita ou da esquerda


# {DIVISÃO DE STRINGS}

# frase.split()
# Vai dividir a string a partir dos caracters de espaços
# lista1 = [Curso] lista2 = [em] lista3 = [Vídeo] lista4 = [Python]


# {JUNÇÃO DE STRINGS}

# '-'.join(frase)
# frase = 'Curso-em-Vídeo-Python'
