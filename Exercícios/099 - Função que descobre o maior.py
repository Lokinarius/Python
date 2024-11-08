#[IMPORTS]
from time import sleep

#[CABEÇALHO]
print("Função que retorna o maior número")
print("================================")

#[ENTRADA DE DADOS]
def maior(* numero):
    contador = maior = 0
    print('Analisando os valores passados..')
    for valor in numero:
        print(f'{valor}', end='')
        sleep(0.5)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


#[PROGRAMA PRINCIPAL]
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)