# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

alunos = ['junior', 'david', 'mateus', 'kayky']

shuffle(alunos)

print(alunos)
