# escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# para salarios superiores a 1.250,00 calcule um aumento de 10%
# para inferiores ou iguais o aumento é de 15%

salario = float(input('digite o seu salario: '))

aumento10 = salario * 10 / 100
salarioaumentado10 = aumento10 + salario
aumento15 = salario * 15 / 100
salarioaumentado15 = aumento15 + salario

if salario >= 1250.00:
    print('-=-' * 20)
    print('seu salario padrão é', salario)
    print('o seu salario aumentou 10%, o salario final é ', salarioaumentado10)
    print('-=-' * 20)
else:
    print('-=-' * 20)
    print('seu salario padrão é', salario)
    print('o seu salario aumentado 15% é ', salarioaumentado15)
    print('-=-' * 20)