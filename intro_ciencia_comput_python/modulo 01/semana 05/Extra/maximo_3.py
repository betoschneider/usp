def maximo(x,y,z):
    if x > y and x > z:
        m = x
    else:
        if y > x and y > z:
            m = y
        else:
            m = z
    return m
