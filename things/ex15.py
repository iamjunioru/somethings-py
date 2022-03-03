# escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado-
# e a quantidade de dias pelos quais ele foi alugado. 
# calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,50 por KM rodado.

dia = int(input('por quantos dias o carro foi alugado? '))
km = float(input('quantos KM foi percorrido com ele? '))

aluguel = 60
rodado = 0.15

resultado1 = dia * aluguel 
resultado2 = km * rodado

total = resultado1 + resultado2

print('o valor total a pagar é R${:.2f}.'.format(total))
