import random
print('QUEM VAI APAGAR O QUADRO?')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f'O aluno escolhido para apagar o quadro é: {escolhido}')
