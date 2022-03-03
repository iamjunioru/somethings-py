# escreva um programa que leia um valor em metros e a exiba convertido em centimetros e milimetros.

m = float(input('distancia em metros: '))

cm = m * 100
mm = m * 1000

print('{}m corresponde a {}cm e {}mm'.format(m, cm, mm))