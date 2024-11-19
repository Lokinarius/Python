# Programa principal
def notas(*n, situacao=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if situacao:
        if r['media'] >= 7:
            r['situacao'] = 'Aprovado'
        elif r['media'] >= 5:
            r['situacao'] = 'Recuperação'
        else:
            r['situacao'] = 'Reprovado'
    return r
resposta = notas(7,8.9,10,5,3, situacao=True)
print(resposta)

