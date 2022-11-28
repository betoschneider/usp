'''Implemente a função fatorial(x), que recebe como parâmetro um número 
inteiro e devolve um número inteiro correspondente ao fatorial de x.

Sua solução deve ser implementada utilizando recursão.'''



def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)