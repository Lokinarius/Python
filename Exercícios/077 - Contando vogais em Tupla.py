palavras = (
    "abacaxi", "banana", "cachorro", "dado", "elefante",
    "foguete", "gato", "hipopotamo", "iguana", "escola"
)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')