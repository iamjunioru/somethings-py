# desenvolva um programa que leia o comprimento de tres retas 
# e diga o usuario se elas podem ou nao =
# formar um triangulo. 

print('*' * 54)
print('------- condição de existência de um triângulo -------'.upper())
print('*' * 54)

r1 = float(input('informe o comprimento da primeira reta: '))
r2 = float(input('informe o comprimento da segunda reta: '))
r3 = float(input('informe o comprimento da terceira reta: '))

sit_1 = ((r2 - r3) < r1 < (r2 + r3))
sit_2 = ((r1 - r3) < r2 < (r1 + r3))
sit_3 = ((r1 - r2) < r3 < (r1 + r2))

if (sit_1 and sit_2 and sit_3):
    print('PARABÉNS! é possível formar um triângulo com essas retas!')
else:
    print('DESCULPA. não é possível formar um triângulo com essas retas.')