# Estruturas Básicas

'''
Uma pesquisa sobre algumas características físicas da população de uma determinada região coletou dados, referentes a
cada habitante, para serem analisados:

 Sexo (m ou f)
 Cor dos olhos (azuis, verdes, castanhos)
 Cor dos cabelos (louros, castanhos, pretos)
 Idade (em anos)

Faça um programa que leia os dados dos habitantes até que seja informado um valor de idade igual a -1.

Oprograma deverá imprimir na tela o número de habitantes do sexo feminino cuja idade esteja entre 18 e 35 anos
inclusive.
'''

idade = 0
sexo = 0
contator = 0

while(idade != -1):
    sexo = int(input('[1 = Masculino | 2 = Feminino] Insira o sexo: '))
    while(sexo > 2 or sexo < 1):
        print('***OPÇÃO INVALIDA***')
        print('** ESCOLHA ENTRE OS NÚMEROS 1 E 2 **')
        sexo = int(input('[1 = Masculino | 2 = Feminino] Insira o sexo: '))
    idade = int(input('Insira a idade: '))
    if(sexo == 2 and idade >= 18 and idade <= 35):
        contator = contator +1
print(f'O número de habitantes do sexo feminino cuja idade esteja entre 18 e 35 é: {contator}')







