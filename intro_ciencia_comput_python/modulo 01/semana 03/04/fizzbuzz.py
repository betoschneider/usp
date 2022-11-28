#fizzbuzz.py

entrada_str = input('Informe um número inteiro: ')

entrada = int(entrada_str)

resto3 = entrada%3

resto5 = entrada%5

if (resto3 == 0) and (resto5 == 0):
    print('FizzBuzz')

else:
    print(entrada_str)
