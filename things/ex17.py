# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
# ...calcule e mostre o comprimento da hipotenusa.

import math

opos = float(input('digite o valor do cateto oposto: '))
adj = float(input('digite o valor do cateto adjacente: '))

hipo = math.hypot(opos, adj)

print('o valor da hipotenusa é {:.2f}'.format(hipo))