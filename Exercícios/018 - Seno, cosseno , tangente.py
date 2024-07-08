print('SENO, COSSENO E TANGENTE')
ang = float(input('Informe um ângulo para definir seu seno, cosseno e tangente: '))
import math
seno = math.radians(math.sin(ang))
# math.radians {serve para converte os angulos em radianos}
# math.sin {serve para medir o seno de um ângulo}
cosseno = math.radians(math.cos(ang))
# math.cos {serve para medir o cosseno de um ângulo}
tangente = math.radians(math.tan(ang))
# math.tan {serve para medir a tangente de um ângulo}
print(f'O seno de {ang}° é {seno}')
print(f'O cosseno de {ang}° é {cosseno}')
print(f'A tangente de {ang}° é {tangente}')