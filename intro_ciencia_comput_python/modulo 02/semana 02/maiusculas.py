def maiusculas(frase):
    maiusculas = ''
    for i in range(len(frase)):
        if ord(frase[i]) >= 65 and ord(frase[i]) < 97:
            maiusculas = maiusculas + frase[i]
    return maiusculas
