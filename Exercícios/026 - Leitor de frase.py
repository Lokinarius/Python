frase = str(input('Escreva uma frase: ')).upper().strip()
print(f'A letra "A" aparece {frase.count('A')} vezes.')
print(f'A primeira posição em que aparece a letra "A" é a {frase.find('A')+1}ª posição')
print(f'A última posição em que aparece a letra "A" é a {frase.rfind('A')+1}ª posição')
