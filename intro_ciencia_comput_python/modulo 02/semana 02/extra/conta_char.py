def conta_letras(frase, contar = 'vogais'):
    vogais = 'aäáâàãeéêëèiíîïìoöóôòõuüúûù'
    consoantes = 'bcçdfghjklmnpqrstvwxyz'
    frase = frase.lower()

    qtd = 0
    if contar == 'vogais':
        for i in range(len(frase)):
            if frase[i] in vogais:
                qtd += 1
    else:
        for i in range(len(frase)):
            if frase[i] in consoantes:
                qtd += 1
    return qtd
