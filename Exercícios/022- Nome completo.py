nome = str(input('Digite um nome completo: '))
print(f'O nome com todas letras maiúsculas  fica: {nome.upper()}')
print(f'O nome com todas letras minúsculas fica: {nome.lower()}')
nome_sem_espacos = nome.replace(' ', '')
print(f'Foi utilizado um total de {len(nome_sem_espacos)} letras')
primeiro_nome = nome.split()[0]
print(f'O primeiro nome tem {len(primeiro_nome)} letras')