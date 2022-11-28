i = input("digite um inteiro positivo :")

n = len(i)

i = int(i)

soma = 0

while n > 0:
    soma = soma + (i % 10)
    i = i // 10
    n = n - 1

print(soma)
    
