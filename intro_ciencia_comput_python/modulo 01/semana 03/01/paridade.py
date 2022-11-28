#paridade.py

entrada_str = input('Informe um número inteiro: ')

entrada = int(entrada_str)

resto = entrada%2

if resto == 0:
    print('par')

else:
    print('ímpar')
