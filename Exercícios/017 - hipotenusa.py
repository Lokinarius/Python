print('CALCULO DA HIPOTENUSA \n')
import math
ca = float(input('Digite o Cateto Adjacente: '))
co = float(input('Digite o Cateto Oposto:'))
hip = math.sqrt((ca**2)+(co**2))
print(f'O resultado do calculo da hipotenusa é {hip:.2f}')