x = input("digite um número inteiro: ")

n = m = len(x)

x = int(x)

adj = False

primeiroDigito = x % 10

while n > 0 and not adj:
    if n == m:
        digitoAnterior = x % 10
        x = x // 10
        n = n - 1
    else:
        digito = x % 10
        if digito == digitoAnterior:
            adj = True
            print('sim')
        digitoAnterior = digito
        x = x // 10
        n = n - 1

if not adj:
    print('não')
