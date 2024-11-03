# FUNÇÕES

# Para se definir uma função em Python se utiliza o comando "def", o nome da função e ()

# [Exemplo simples]
nome = input("Digite seu nome: ")
def linha():
    print("-" * 20)
def saudacao():
    print(f'Olá,{nome} seja bem-vindo!')
linha()
saudacao()
linha()


# [Exemplo com argumentos]
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Erro"
    return a / b
def calcular():
    print("1.Soma")
    print("2.Subtração")
    print("3.Multiplicação")
    print("4.Divisão")
    operacao = int(input("Escolha uma opção: "))
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Digite um número.")
        return
    if operacao == 1:
        print(f"Resultado: {somar(num1, num2)}")
    elif operacao == 2:
        print(f"Resultado: {subtrair(num1, num2)}")
    elif operacao == 3:
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif operacao == 4:
        print(f"Resultado: {dividir(num1, num2)}")
    else:
        print("Opção inválida!")
linha()
calcular()
linha()
