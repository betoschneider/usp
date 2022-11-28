'''
Implemente a função busca(lista, elemento), que busca um determinado elemento 
em uma lista e devolve o índice correspondente à posição do elemento encontrado. 
Utilize o algoritmo de busca binária. Nos casos em que o elemento buscado não 
existir na lista, a função deve devolver o booleano False.

Além de devolver o índice correspondente à posição do elemento encontrado, sua 
função deve imprimir cada um dos índices testados pelo algoritmo
'''

def insertion_sort(lista):
    ordem = False
    i = 0
    
    while not ordem:
        ordem = True
        for i in range(len(lista)):
            if i > 0:
                if lista[i] < lista[i - 1]:
                    ordem = False
                    lista[i], lista[i - 1] = lista[i - 1], lista[i]
                    
                    #print(lista)
        
    return lista
    
        