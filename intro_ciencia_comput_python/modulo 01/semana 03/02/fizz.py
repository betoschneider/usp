#fizz.py

entrada_str = input('Informe um número inteiro: ')

entrada = int(entrada_str)

resto = entrada%3

if resto == 0:
    print('Fizz')

else:
    print(entrada_str)
