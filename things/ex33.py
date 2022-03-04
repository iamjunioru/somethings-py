# faça um programa que leia três numeros e mostre qual é o maior e qual é o menor.

primeiro = int(input('digite o primeiro número:'))
segundo = int(input('digite o segundo número:'))
terceiro = int(input('digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]

print('o maior valor digitado foi {}'.format(max(numeros)))
print('o menor numero digitado foi {}'.format(min(numeros)))