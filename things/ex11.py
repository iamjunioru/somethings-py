# faça um programa que leia a largura e a  altura de uma parede em metros.
# calcule a sua area e a quantidade de tinta necessaria para pinta-la.
# sabendo-se que cada litro de tinta pinta uma area de 2m.

largura = float(input('digite o valor da largura: '))
altura = float(input('digite o valor da altura: '))

area = largura * altura # calcular a area da parede

print('a largura da parede é {}m e a altura é {}m, ja a area da parede é {}m²'.format(largura, altura, area))

tinta = area / 2

print('a tinta necessária para pintar a parede é {}L de tinta'.format(tinta))