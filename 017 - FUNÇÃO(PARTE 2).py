from time import sleep
def contador(inicio,fim,passo):
    print(f'\nContagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio < fim:
        for i in range(inicio,fim + 1, passo):
            print(f'{i}', end =' ')
            sleep(0.1)
    else:
        for i in range(inicio, fim - 1, -passo):
            print(f'{i}', end =' ')
            sleep(0.1)

contador(2,10,2)
contador(0,100,10)
contador(99,0,3)


# PARAMETROS OPCIONAIS
