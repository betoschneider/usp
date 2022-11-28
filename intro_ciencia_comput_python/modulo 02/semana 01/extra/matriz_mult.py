def sao_multiplicaveis(m1, m2):
    if (len(m1) == len(m2[0])) and (len(m1[0]) == len(m2)):
        return True
    return False
