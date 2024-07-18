print('\tAPROVADO, REPROVADO, RECUPERAÇÃO')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-')

# Nota do aluno
nota1 = float(input('Qual a primeira nota: '))
nota2 = float(input('Qual a segunda nota: '))
media = (nota1 + nota2) / 2

# Classificação do aluno
if media >= 7:
    print(f'A média do aluno foi {media:.1f}')
    print('O aluno está APROVADO')
elif media < 4:
    print(f'a média do aluno foi {media:.1f}')
    print('O aluno está REPROVADO')
else:
    print(f'A média do aluno foi {media:.1f}')
    print('O aluno irá realizar a prova de RECUPERAÇÃO')
