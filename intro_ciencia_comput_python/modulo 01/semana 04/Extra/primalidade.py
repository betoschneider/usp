x = int(input("Digite um número: "))

if x < 0:
    x = -x

primo = True

if x != 2:
    y = (x // 2) + 1

    while y > 1 and primo:
        if x % y == 0:
            primo = False
            print('não primo')
        y = y - 1

if primo:
    print('primo')
    
