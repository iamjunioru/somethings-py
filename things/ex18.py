# faça um programa que leia um angulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse angulo.

import math

an = float(input('digite o angulo que deseja: '))
r = math.radians(an)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)

print('se o angulo for {} \n o seno será {:.3f} \n o coseno será {:.3f} \n e a trangente será {:.3f}'.format(an, s, c, t))