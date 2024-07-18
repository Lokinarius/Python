print('\tMAIOR E MENOR')
print('-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=')
# inserção de dados
num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))
# verificando qual é o maior e qual é o menor
if num1 == num2:
    print('Não existe valor maior, os dois números são iguais')
elif num1 > num2:
    print(f'O número {num1} é maior que o {num2}')
else:
    print(f'O número {num2} é maior que o {num1}')
