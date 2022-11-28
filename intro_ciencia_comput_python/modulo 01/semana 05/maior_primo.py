def maior_primo(x):
    i = 1
    if x < 0:
        x = -x
    
    while i <= x:
        #primo = True
        #y = (i // 2) + 1
        y = 1
        p = 0
        while y <= i: # and primo:
            if i % y == 0:
                p = p + 1
            y = y + 1
        if p <= 2:
            primo = i
        i = i + 1
    if x == 0:
        primo = 0
    return primo
                
                


        
