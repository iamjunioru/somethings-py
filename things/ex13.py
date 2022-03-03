# faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.

salario = float(input('qual o seu salario? R$'))

aumento = salario * 15 / 100
resultado = aumento + salario

print('seu salario final com o aumento de 15% é de {:.2f}.'.format(resultado))