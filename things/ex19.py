# um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# faça um programa que ajude ele::
# lendo o nome deles e escrevendo o nome escolhido.

import random

alunos = ['junior', 'david', 'mateus', 'kayky'] # colchetes deixa como uma lista, mas funciona sem tbm.

escolhidos = random.choice(alunos)

print('o aluno escolhido foi o {}.'.format(escolhidos))