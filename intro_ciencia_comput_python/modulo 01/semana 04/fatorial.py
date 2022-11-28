n = int(input("Digite um número natural n: "))

fatorial = n
d = 1

if n != 0:
    while n > 0:
        if n <= 1:
            n = 2
            d = 3
        fatorial = fatorial * (n - 1)
        n = n - d
else:
    fatorial = 1

print(fatorial)
