def n_primos(n):
    if n < 0:
        n = -n
    x = 1
    primo = True
    p = 0

    while x <= n:
        if x > 2:
            y = (x // 2) + 1

            while y > 1 and primo:
                if x % y == 0:
                    primo = False
                y = y - 1
                
        

        if primo:
            p = p + 1
        primo = True
        x = x + 1
    return p - 1
