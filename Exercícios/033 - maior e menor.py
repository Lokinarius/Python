num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if num1 == num2 == num3:
    print('Todos os números são iguais!')
else:
    menor = num1
    maior = num1
    # Menor número
    if num2 < num1 and num2 < num3:
        menor = num2
    if num3 < num1 and num3 < num2:
        menor = num3

    if num2 > num1 and num2 > num3:
        maior = num2
    if num3 > num1 and num3 > num2:
        maior = num3

print(f'{maior} é o maior número, e {menor} é o menor número.')