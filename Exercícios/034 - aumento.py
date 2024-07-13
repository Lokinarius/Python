salario = float(input('Informe o salário do funcionário: R$'))
if salario >= 1250:
    aumento = (salario/100) * 10
else:
    aumento = (salario/100) * 15
novo_salario = salario + aumento
print(f'O novo salário do funcionário é R${novo_salario:.2f}')

