def ordenada(lista):
    listaOrdenada = sorted(lista)
    for i in range(len(lista)):
        if lista[i] != listaOrdenada[i]:
            return False
    return True
        
        