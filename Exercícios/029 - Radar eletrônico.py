import random
speed = random.randint(20,180)
veloz = f'A velocidade do veículo foi de {speed}km/h \n'
multa = 0.0
if speed <= 80:
    print(f'{veloz}O veículo está dentro do limite de velocidade ')
else:
    multa += (speed - 80) * 7.0
    print(f'{veloz}O veículo está acima da velocidade permitida.\nUma multa de R${multa} será aplicada')
