from datetime import datetime
print('CATEGORIAS DE IDADE')
ano = int(input('Em que ano o atleta nasceu? '))
ano_atual = datetime.now().year
idade = ano_atual - ano
if idade < 8:
    print('Categoria MIRIM')
elif idade <= 12:
    print('Categoria INFANTIL')
elif idade <= 14:
    print('Categoria INFANTO-JUVENIL')
elif idade <= 18:
    print('Categoria JUVENIL')
elif idade <= 20:
    print('Categoria JUNIOR')
elif idade <= 35:
    print('Categoria ADULTO')
else:
    print('Categoria MASTER')