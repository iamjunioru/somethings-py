# crie um algoritmo que leia um numero em mostre o seu dobro, seu triplo e sua raiz quadrada.

n1 = int(input('digite um valor: '))

print('o valor é {}.'.format(n1))
print('o dobro de {} é {}.'.format(n1, n1 * 2))
print('o triplo de {} é {}.'.format(n1, n1 * 3))
print('a raiz quadrada de {} é {:.3f}.'.format(n1, n1 ** (1/2)))