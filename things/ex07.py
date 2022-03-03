# desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.

n1 = float(input('qual a sua primeira nota?\n'))
n2 = float(input('qual a sua segunda nota?\n'))

media = (n1 + n2) / 2

print('a media das notas é {:.2f}, parabéns!'.format(media))