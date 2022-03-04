# desenvolva um programa que pergunte a distancia de uma viagem em KM. calcule o preço da passagem
# cobrando R$0,50 por KM para viajens de ate 200KM e R$0,45 para viagens mais longas.

km = float(input('digite quantos KM você viajou: '))

viagem200 = km * 0.50
viagemlong = km * 0.45

if km <= 200:
    print('sua viagem de 200KM custa: R${:.2f}'.format(viagem200))
else:
    print('sua viagem de mais de 200KM custa: R${:.2f}'.format(viagemlong))