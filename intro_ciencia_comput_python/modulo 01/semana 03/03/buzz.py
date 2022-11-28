#buzz.py

entrada_str = input('Informe um número inteiro: ')

entrada = int(entrada_str)

resto = entrada%5

if resto == 0:
    print('Buzz')

else:
    print(entrada_str)
