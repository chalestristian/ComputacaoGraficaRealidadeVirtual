# Estruturas Básicas

'''
Faça um programa que receba dois números e execute as operações listadas a seguir, de acordo com a escolha do usuário.

Escolha     Operação
1           Média entre os números digitados
2           Diferença do maior pelo menor
3           Produto entre os números digitados
4           Divisão do primeiro pelo segundo

Se a opção digitada for inválida, mostre uma mensagem de erro.
Lembre-se de que, na opção 4, o segundo número deve ser diferente de zero.
'''

numum = float(input('Informe o primeiro numero: '))
numdois = float(input('Informe o segundo numero: '))
opcao = int(input('Escolha uma opcao de 1 a 4: '))

while(opcao < 1 or opcao > 4):
    print('**OPÇÃO INVALIDA**')
    opcao = int(input('*Escolha uma opcao de 1 a 4: '))

if(opcao == 1):
    resultado = (numum+numdois)/2
    print(f'A média entre o numero {numum} e {numdois} é: {resultado}')
elif(opcao == 2):
    if (numum > numdois):
        resultado = numum - numdois
        print(f'A diferença do numero {numum} e {numdois} é: {resultado}')
    else:
        resultado = numdois - numum
        print(f'A diferença do numero {numdois} e {numum} é: {resultado}')
elif(opcao == 3):
    resultado = numum * numdois
    print(f'O produto entre o numero {numum} e {numdois} é: {resultado}')
elif(opcao == 4):
    if(numdois == 0):
        print('ERRO: O segundo número não pode ser igual a zero!')
    else:
        resultado = numum / numdois
        print(f'O resultado da divisão do numero {numdois} por {numum} é: {resultado}')

