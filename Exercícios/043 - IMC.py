print('\tIMC')
# inserção de dados
peso = float(input('Quanto você pesa ? '))
altura = float(input('Qual a sua altura ? '))
# cálculo do IMC
imc = peso / (altura * altura)
# classificação do IMC
if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}, você está abaixo do peso!')
elif imc <= 25:
    print(f'Seu IMC é de {imc:.2f}, você se encontra no seu peso ideal!')
elif imc <= 30:
    print(f'Seu IMC é de {imc:.2f}, você está em sobrepeso!')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.2f}, você está em obesidade!')
else:
    print(f'Seu IMC é de {imc:.2f}, você está em obesidade mórbida!')
