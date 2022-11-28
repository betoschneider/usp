#lista=[1,2,5,4,5,7,0,0,5]
def remove_repetidos(lista):
    lista2 = []
    lista2.append(lista[0])
    repetido = False
    for i in range(len(lista)):
        for j in range(len(lista2)):
            if lista[i] == lista2[j]:
                repetido = True
        if not repetido:
            lista2.append(lista[i])
            #repetido = False
        repetido = False
    lista2.sort()
                
    return lista2
    
