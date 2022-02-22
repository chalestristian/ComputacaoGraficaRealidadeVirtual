# Estruturas Básicas

'''
Escreva um programa que seja capaz de ler do teclado 31 valores reais correspondentes ao índice pluviométrico
diário de um mês. O programa deve determinar o índice pluviométrico médio, o índice pluviométrico máximo e o
dia de ocorrência.
'''

media = 0
total = 0
indicemaximo = 0
diaindicemaximo = 0
for i in range(31):
    indice = float(input(f'Informe o indice do dia {i+1}: '))
    total = indice + total
    media = total / 5
    if(indice > indicemaximo):
        diaindicemaximo = i+1
        indicemaximo = indice

print(f'O índice pluviométrico médio é: {media}')
print(f'O índice pluviométrico máximo ocorreu no dia {diaindicemaximo} e foi de {indicemaximo}')
