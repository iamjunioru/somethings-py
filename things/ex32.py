# faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import calendar

ano = int(input('Digite o ano: '))

ano6 = calendar.isleap(ano)

if ano6 is True:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')