#pontos.py

entrada1_str = input('Informe a primeira coordenada do primeiro ponto: ')
entrada2_str = input('Informe a segunda coordenada do primeiro ponto: ')
entrada3_str = input('Informe a primeira coordenada do segundo ponto: ')
entrada4_str = input('Informe a segunda coordenada do segundo ponto: ')

px1 = float(entrada1_str)
py1 = float(entrada2_str)
px2 = float(entrada3_str)
py2 = float(entrada4_str)

distancia = ((px1 - px2)**2 + (py1 - py2)**2)**(1/2)

if distancia >= 10:
    print('longe')

else:
    print('perto')

