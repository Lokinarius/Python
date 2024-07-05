larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print(f'Sua parede tem a dimensão de {larg} X {alt} e sua área é de {area:.2f} m².')
print(f'Para pintar essa parede você precisará de {tinta:.2f}l de tinta.')
