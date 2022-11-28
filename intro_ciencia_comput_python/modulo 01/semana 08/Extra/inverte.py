#lista=[1,2,5,4,5,7,0,0,5]
lista = []
ordem = []
m = 0
n = int(input('Digite um número qualquer ou zero pra terminar: '))
while n != 0:
    lista.append(n)
    ordem.append(m)
    m = m + 1
    n = int(input('Digite um número qualquer ou zero pra terminar: '))
ordem.sort(reverse=True)
for i in ordem:
    print(lista[i])
    
