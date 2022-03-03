# escreva um programa que converta uma temperatura digitada em celsius e converta para fahrenheith.

cel = float(input('digite algum valor em celsius: '))

conversao = cel * 1.8 + 32

print('o valor de {}°C em fahrenheith é {:.1f}°F'.format(cel, conversao))