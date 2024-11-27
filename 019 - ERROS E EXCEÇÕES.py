# Lista ampliada de exceções comuns em Python com explicação
def excecoes_python_ampliada():
    try:
        # Exceção: SyntaxError
        # Ocorre quando há um erro na sintaxe do código.
        eval("x === y")  # Exemplo de código com erro de sintaxe
    except SyntaxError as e:
        print("SyntaxError: Erro na sintaxe do código.")

    try:
        # Exceção: NameError
        # Ocorre quando uma variável ou função não está definida.
        print('variavel inexistente')
    except NameError as e:
        print("NameError: Tentativa de acessar uma variável ou função que não existe.")

    try:
        # Exceção: TypeError
        # Ocorre quando uma operação ou função recebe um tipo de dado inválido.
        resultado = "string" + 5
    except TypeError as e:
        print("TypeError: Operação inválida para os tipos fornecidos.")

    try:
        # Exceção: ValueError
        # Ocorre quando uma função recebe um valor válido, mas inapropriado.
        numero = int("texto")
    except ValueError as e:
        print("ValueError: Conversão ou operação com valor inválido.")

    try:
        # Exceção: IndexError
        # Ocorre quando um índice é usado fora dos limites de uma lista ou tupla.
        lista = [1, 2, 3]
        elemento = lista[5]
    except IndexError as e:
        print("IndexError: Índice fora dos limites de uma lista ou tupla.")

    try:
        # Exceção: KeyError
        # Ocorre quando se tenta acessar uma chave inexistente em um dicionário.
        dicionario = {"chave": "valor"}
        valor = dicionario["chave_inexistente"]
    except KeyError as e:
        print("KeyError: Chave inexistente no dicionário.")

    try:
        # Exceção: AttributeError
        # Ocorre quando se tenta acessar um atributo inexistente de um objeto.
        objeto = 10
        objeto.atributo = "valor"
    except AttributeError as e:
        print("AttributeError: Tentativa de acessar um atributo inválido de um objeto.")

    try:
        # Exceção: ZeroDivisionError
        # Ocorre quando se tenta dividir um número por zero.
        resultado = 10 / 0
    except ZeroDivisionError as e:
        print("ZeroDivisionError: Divisão por zero não é permitida.")

    try:
        # Exceção: FileNotFoundError
        # Ocorre quando um arquivo especificado não é encontrado.
        with open("arquivo_inexistente.txt", "r") as file:
            conteudo = file.read()
    except FileNotFoundError as e:
        print("FileNotFoundError: Arquivo não encontrado.")

    try:
        # Exceção: ImportError
        # Ocorre quando uma importação falha.
        import modulo_inexistente
    except ImportError as e:
        print("ImportError: Módulo ou biblioteca não encontrado.")

    try:
        # Exceção: OSError
        # Ocorre para erros relacionados ao sistema operacional.
        import os
        os.remove("/caminho/arquivo_inexistente")
    except OSError as e:
        print("OSError: Erro ao realizar operações no sistema operacional.")

    # Novas Exceções Adicionadas

    try:
        # Exceção: IndentationError
        # Ocorre quando há erro na indentação do código.
        exec("def func():\nreturn 1")  # Código com indentação incorreta
    except IndentationError as e:
        print("IndentationError: Erro na indentação do código.")

    try:
        # Exceção: ModuleNotFoundError
        # Subclasse de ImportError, ocorre quando um módulo específico não é encontrado.
        import modulo_inexistente_especifico
    except ModuleNotFoundError as e:
        print("ModuleNotFoundError: Módulo específico não encontrado.")

    try:
        # Exceção: RuntimeError
        # Ocorre quando uma condição de erro que não se enquadra em outras categorias é detectada.
        raise RuntimeError("Erro de tempo de execução.")
    except RuntimeError as e:
        print("RuntimeError: Erro de tempo de execução.")

    try:
        # Exceção: NotImplementedError
        # Ocorre quando uma funcionalidade ainda não foi implementada.
        class Base:
            def metodo(self):
                raise NotImplementedError("Método não implementado.")
        obj = Base()
        obj.metodo()
    except NotImplementedError as e:
        print("NotImplementedError: Funcionalidade ainda não implementada.")

    try:
        # Exceção: AssertionError
        # Ocorre quando uma asserção falha.
        assert 2 + 2 == 5, "A soma está incorreta."
    except AssertionError as e:
        print("AssertionError: Falha na asserção.")

    try:
        # Exceção: MemoryError
        # Ocorre quando o sistema não tem memória suficiente para executar uma operação.
        lista_grande = [0] * (10**10)
    except MemoryError as e:
        print("MemoryError: Memória insuficiente para executar a operação.")

    try:
        # Exceção: FloatingPointError
        # Ocorre para erros relacionados a operações de ponto flutuante.
        import math
        math.exp(1000)  # Pode causar overflow
    except FloatingPointError as e:
        print("FloatingPointError: Erro em operação de ponto flutuante.")

    try:
        # Exceção: RecursionError
        # Ocorre quando a profundidade máxima de recursão é excedida.
        def recursao_infinita():
            return recursao_infinita()
        recursao_infinita()
    except RecursionError as e:
        print("RecursionError: Profundidade máxima de recursão excedida.")

    try:
        # Exceção: KeyboardInterrupt
        # Ocorre quando o usuário interrompe a execução (por exemplo, pressionando Ctrl+C).
        import time
        print("Pressione Ctrl+C para interromper.")
        time.sleep(10)
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt: Execução interrompida pelo usuário.")

    try:
        # Exceção: EOFError
        # Ocorre quando a função input() atinge o fim do arquivo sem ler dados.
        import sys
        sys.stdin = open(os.devnull)  # Redireciona stdin para vazio
        input("Digite algo: ")
    except EOFError as e:
        print("EOFError: Fim do arquivo atingido sem leitura de dados.")

    try:
        # Exceção: UnicodeEncodeError
        # Ocorre quando ocorre um erro ao codificar uma string Unicode.
        s = "áéíóú"
        s.encode("ascii")
    except UnicodeEncodeError as e:
        print("UnicodeEncodeError: Erro ao codificar string Unicode.")

    try:
        # Exceção: UnicodeDecodeError
        # Ocorre quando ocorre um erro ao decodificar uma sequência de bytes.
        b = b'\xff'
        b.decode('utf-8')
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError: Erro ao decodificar bytes para string Unicode.")

    try:
        # Exceção: UnicodeTranslateError
        # Ocorre quando ocorre um erro ao traduzir caracteres Unicode.
        s = "你好"
        s.encode('ascii', 'translate')
    except UnicodeTranslateError as e:
        print("UnicodeTranslateError: Erro ao traduzir caracteres Unicode.")

    try:
        # Exceção: StopIteration
        # Ocorre quando a iteração não tem mais itens para retornar.
        iterador = iter([1, 2])
        print(next(iterador))
        print(next(iterador))
        print(next(iterador))  # Isso gerará StopIteration
    except StopIteration as e:
        print("StopIteration: Iterador não tem mais itens.")

    try:
        # Exceção: LookupError
        # Classe base para erros relacionados a buscas, como KeyError e IndexError.
        raise LookupError("Erro de busca genérico.")
    except LookupError as e:
        print("LookupError: Erro genérico de busca.")

# Executar a função para exibir as exceções e explicações
excecoes_python_ampliada()