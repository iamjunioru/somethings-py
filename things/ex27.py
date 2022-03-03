# faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome separadamente.
# ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

n = str(input('digite seu nome completo: ')).strip()

nome = n.split()

print('prazer em te conhecer!')
print('seu primeiro nome é {}.'.format(nome[0]))
print('seu ultimo nome é {}.'.format(nome[len(nome)-1]))