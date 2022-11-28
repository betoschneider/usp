#ordenacao.py

entrada1_str = input('Informe um número inteiro: ')
entrada2_str = input('Informe outro número inteiro: ')
entrada3_str = input('Informe mais um número inteiro: ')

entrada1 = int(entrada1_str)
entrada2 = int(entrada2_str)
entrada3 = int(entrada3_str)

if (entrada2 > entrada1) and (entrada3 > entrada2):
    print('crescente')

else:
    print('não está em ordem crescente')
