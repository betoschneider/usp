segundos_str = input('Por favor, entre com o número de segundos que deseja converter: ')

segundos = int(segundos_str)

dias = segundos // (3600 * 24)

segundos = segundos % (3600 * 24)

horas = segundos // 3600

segundos = segundos % 3600

minutos = segundos // 60

segundos = segundos % 60

print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', segundos, 'segundos.')



