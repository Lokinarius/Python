salario = float(input('qual é o salário do funcionário? R$'))
aumento = 15 * (salario/100)
valor = salario + aumento
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${valor:.2f}')