n = int(input("Digite um número natural n: "))

i = 1

while n != 0:
    if i % 2 != 0:
        print(i)
        n = n - 1
    i = i + 1
