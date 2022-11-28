def menor_nome(lista):
    menor = 9999999999
    for i in range(len(lista)):
        if len(lista[i].strip()) < menor:
            menor = len(lista[i].strip())
            palavra = lista[i].strip().capitalize()
    return palavra
