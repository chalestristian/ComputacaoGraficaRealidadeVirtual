# Estruturas Básicas

'''
Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Leia a massa inicial, em
gramas, faça um programa que determine o tempo necessário para que essa massa se torne menor do que 0,5
grama. Escreva a massa inicial, massa final e o tempo calculado.
'''

massainicial = float(input('Informe a massa em gramas: '))
massafinal = massainicial
tempo = 0
while(massafinal > 0.5):
    massafinal = massafinal / 2
    tempo = tempo + 50

print(f'Massa inicial era: {massainicial}')
print(f'Tempo calculado foi: {tempo}')
print(f'Massa final é: {massafinal}')

