# Estruturas Básicas

'''
Faça um algoritmo que informe o mês de acordo com o número digitado pelo usuário.
Exemplo: Entrada = 4.
Saída = Abril.
'''

numero = int(input('Insira um número de 1 a 12 para saber o mês: '))
while(numero < 1 or numero > 12):
    print('***NÚMERO INVÁLIDO!')
    numero = int(input('**Insira um número entre 1 a 12 para saber o mês: '))

meses = [' ','Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

print(f'O número {numero} é equivalente ao mês de', meses[numero])