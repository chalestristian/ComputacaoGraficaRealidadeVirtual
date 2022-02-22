'''
Faça um programa que apresente o menu de opções a seguir, que permita ao usuário escolher a opção desejada,
receba os dados necessários para executar a operação e mostre o resultado.

Menu de opções:
1) Novo salário
2) Férias
3) Décimo terceiro
4) Sair

Na opção 1:
Receber o salário de um funcionário, calcular e mostrar o novo salário usando as regras a seguir:
Salários                    Percentagem de aumento
Até R$999,99                15%
De R$1000,00 a R$2000,00    10%
Acima de R$2000,00          5%

Na opção 2:
receber o salário de um funcionário, calcular e mostrar o valor de suas férias.
Sabe-se que as férias equivalem a seu salário acrescido de um terço do salário.

Na opção 3:
receber o salário de um funcionário e o número de meses de trabalho na empresa, no máximo doze,
calcular e mostrar o valor do décimo terceiro.
Sabe-se que o décimo terceiro equivale a seu salário multiplicado pelo número de meses de trabalho dividido por 12.

Na opção 4:
Sair do programa

Obs: caso seja informada uma opção ou um salário inválido deve-se apresentar uma mensagem de erro e solicitar um novo valor.'''

print('## MENU DE OPÇÕES ##')
print(' 1) Novo salário')
print(' 2) Férias')
print(' 3) Décimo terceiro')
print(' 4) Sair')
opcao = int(input('- Escolha uma opção [somente número]: ' ))
while(opcao<1 or opcao >4):
    print('*************************************************')
    print('OPÇÃO ERRADA!!! SELECIONE UM DOS NÚMEROS ABAIXO')
    print('## MENU DE OPÇÕES ##')
    print(' 1) Novo salário')
    print(' 2) Férias')
    print(' 3) Décimo terceiro')
    print(' 4) Sair')
    opcao = int(input('- Escolha uma opção [SOMENTE O NUMERO]: '))


if(opcao == 1):
    salario = float(input('- Informe o seu salário: '))
    if(salario <= 999.99):
        salario = salario / 100 * 115
        print(f'Seu novo salário é {salario}')
    elif(salario >= 1000.00 and salario < 2000.00):
        salario = salario / 100 * 110
        print(f'Seu novo salário é {salario}')
    elif(salario >= 2000.00):
        salario = salario / 100 * 105
        print(f'Seu novo salário é {salario}')
    else:
        print(f'Seu salário permanece {salario}')

if(opcao == 2):
    salario = float(input('- Informe o seu salário: '))
    umterco = salario / 3;
    ferias = salario + umterco;
    print(f' Você receberá de férias o valor de: {ferias} ')

if(opcao == 3):
    salario = float(input('- Informe o seu salário: '))
    mesestrabalhados = float(input('- Informe o número de meses trabalhados: '))
    while(mesestrabalhados <=0 or mesestrabalhados > 12 ):
        print('*************************************************')
        print('OPÇÃO ERRADA!!! INFORME UM NÚMERO DE 0 A 12:')
        mesestrabalhados = float(input('- Informe o número de meses trabalhados: '))
    decimoterceiro = salario*mesestrabalhados/12;
    print(f'Seu decimo terceiro é de: {decimoterceiro}')
