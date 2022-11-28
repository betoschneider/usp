#bhaskara.py

a_str = input('Informe o valor de a: ')
b_str = input('Informe o valor de b: ')
c_str = input('Informe o valor de c: ')

a = float(a_str)
b = float(b_str)
c = float(c_str)

delta = b**2 - (4 * a * c)

if delta >= 0:
    x1 = (-b + delta**(1/2))/(2 * a)
    x2 = (-b - delta**(1/2))/(2 * a)

    if delta == 0:
        print('a raiz desta equação é', x1)
    else:
        if x1 < x2:
            print('as raízes da equação são', x1, 'e', x2)
        else:
            print('as raízes da equação são', x2, 'e', x1)
else:
    print('esta equação não possui raízes reais')
