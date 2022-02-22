# Estruturas Básicas

'''
Faça um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha
da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e
efetuar o cálculo adequado.

Código Condição de pagamento:
1 - À vista em dinheiro, recebe 10% de desconto.
2 - À vista no cartão de crédito, recebe 5% de desconto.
3 - Em 2 vezes, preço normal de etiqueta sem juros.
4 - Em 3 vezes, preço normal de etiqueta mais 10% de juros.
'''

preco = float(input('Insira o valor do produto: '))
cod = float(input('Insira o código referente a condição de pagamento: '))

if(cod == 1):
    valorapagar = (preco/100)*90
    print(f'Compra á vista em dinheiro. Desconto de 10%: R$ {valorapagar}')
elif(cod == 2):
    valorapagar = (preco/100)*95
    print(f'Compra á vista no crédito. Desconto de 5%: R$ {valorapagar}')
elif (cod == 3):
    valorapagar = preco
    print(f'Compra dividida em 2x. Peço da etiqueta sem descontos ou juros: R$ {valorapagar}')
elif(cod == 4):
    valorapagar = (preco/100)*110
    print(f'Compra dividida em 3x. Peço da etiqueta + 10% de juros: R$ {valorapagar}')
else:
    print('Código de condição de pagamento não existe. Tente novamente.')