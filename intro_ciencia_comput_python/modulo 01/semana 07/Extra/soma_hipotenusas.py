def é_hipotenusa(a):
    b = 1
    c = 1
    hipotenusa = False

    while b <= a:
        while c <= a:
            if a**2 == (b**2 + c**2):
                hipotenusa = True
                #print('b =',b,'c =',c,'=>', (b**2 + c**2),hipotenusa)
            c = c + 1
        b = b + 1
        c = 1
    return hipotenusa
                
                
            
        
def soma_hipotenusas(n):
    if n < 0:
        n = -n
    if n <= 1:
        return 0
    i = 1
    h = 0
    while i <= n:
        if é_hipotenusa(i):
            h = h + i
        i = i + 1
    return h
