# faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra 'a';
# em que posição aparece a primeira vez;
# em que posição ela aparece a ultima vez;

nome = str(input('digite seu nome: ')).upper().strip()

print('a letra A aparece {} vez(es)'.format(nome.count('A')))

print('a letra A apareceu na posição {}.'.format(nome.find('A')+1))

print('a ultima letra A apareceu na posição {}'.format(nome.rfind('A')+1))