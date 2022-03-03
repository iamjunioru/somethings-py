# escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80Km/h, mostre uma mensagem que foi multado:
# a multa vai custar 7 reais por cada KM acima do limite.

vel = float(input('Qual a velocidade do carro? '))

if vel >= 80:
    print('você foi multado em R${:.2f}'.format((vel - 80) * 7.00))
    print("dirija um pouco mais devagar.")
else:
    print('muito bem!')
    print('você está abaixo de 80Km/h e não foi multado.')