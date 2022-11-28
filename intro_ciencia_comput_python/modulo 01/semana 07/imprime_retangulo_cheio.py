l = int(input('Informe a largura l: '))
h = int(input('Informe a altura h: '))

n = 0
m = 0

while n < h:
    while m < l:
        print('#',end='')
        m = m + 1
    print()
    m = 0
    n = n + 1
