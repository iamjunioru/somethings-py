# crie um programa que leia quanto dinheiro uma pessoa tem na carteira --
#  e mostra quantos dolares ela pode comprar --
# considere que o dolar está R$5,15.

n = float(input("Quanto dinheiro você tem? \nR$"))

dolar = 5.15
conversao = n / dolar

print("com R${:.2f} você pode comprar US${:.2f}.".format(n, conversao))