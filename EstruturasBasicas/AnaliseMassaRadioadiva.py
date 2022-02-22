# Estruturas Básicas

'''
Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Leia a massa inicial, em
gramas, faça um programa que determine o tempo necessário para que essa massa se torne menor do que 0,5
grama. Escreva a massa inicial, massa final e o tempo calculado.
'''

massainicial = float(input('Informe a massa em gramas: '))
massaatual = massainicial
tempo = 0
while(massaatual > 0.5):
    massaatual = massaatual / 2
    tempo = tempo + 50
    print('-------------')
    print(f'Massa atual: {massaatual}g')
    print(f'Tempo atual: {tempo}s')
print('*************************************')
print(f'Massa inicial era: {massainicial}g')
print(f'Tempo calculado foi: {tempo}s')
print(f'Massa final é: {massaatual}g')

