# crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR.

numero = int(input('digite um numero: '))

resultado = numero % 2

if resultado == 0:
    print('o resultado é PAR ', numero)
else:
    print('o resultado é IMPAR', numero)