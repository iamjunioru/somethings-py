# crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome.

nome = str(input('qual é o seu nome completo? ')).strip()


print('silva' in nome.lower())