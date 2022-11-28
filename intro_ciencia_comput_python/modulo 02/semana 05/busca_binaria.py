'''
Implemente a função busca(lista, elemento), que busca um determinado elemento 
em uma lista e devolve o índice correspondente à posição do elemento encontrado. 
Utilize o algoritmo de busca binária. Nos casos em que o elemento buscado não 
existir na lista, a função deve devolver o booleano False.

Além de devolver o índice correspondente à posição do elemento encontrado, sua 
função deve imprimir cada um dos índices testados pelo algoritmo
'''

def busca(lista, elemento):
    a = 0
    n = len(lista) - 1
    
    while a <= n:
        meio = ((a + n) // 2)
        print(lista[meio] - 1) #valor
        if lista[meio] == elemento:
            return meio    #indice
        else:
            if elemento < lista[meio]:
                n = meio - 1
            else:
                a = meio + 1
    return False