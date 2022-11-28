entrada = input('Digite um número inteiro: ')

x = int(entrada)
y = x - ((x//100)*100)
dezena = y // 10

print('O dígito das dezenas é',dezena)

