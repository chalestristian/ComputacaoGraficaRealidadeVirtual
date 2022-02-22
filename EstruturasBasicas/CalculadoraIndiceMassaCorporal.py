# Estruturas Básicas

'''
O IMC - Índice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação de
peso de uma pessoa adulta. A fórmula é IMC = peso/(altura)2

Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição.

IMC em adultos Condição
abaixo de 18,5 abaixo do peso
entre 18,5 e 25 peso normal
entre 25 e 30 acima do peso
acima de 30 obeso
'''

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso/(altura)**2

print(imc)

if (imc < 18.5):
    print(f'Seu indice de massa corporal é {imc}. Você está abaixo do peso')
elif (imc < 25):
    print(f'Seu indice de massa corporal é {imc}. Você está no seu peso normal')
elif(imc < 30):
    print(f'Seu indice de massa corporal é {imc}. Você está acima do peso')
else:
    print(f'Seu indice de massa corporal é {imc}. Você está obeso')
