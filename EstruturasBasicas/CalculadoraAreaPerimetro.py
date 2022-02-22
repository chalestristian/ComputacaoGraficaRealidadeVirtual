# Estruturas Básicas

'''
Crie um programa para calcular a área e o perímetro de um retângulo, com base nas medidas de sua base e de sua altura.
'''

base = int(input('Digite a base do retangulo: '))
altura = int(input('Digite a altura do retangulo: '))

area = base * altura;
perimetro = (base*2) + (altura*2);

print(f'A base do retengulo é {base} e a altura é {altura}');
print(f'A area do retangulo é {area} e o perímetro é {perimetro}')