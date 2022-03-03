# crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas;
# com todas as letras minusculas;
# quantas letras ao todo(sem considerar os espaços);
# quantas letras tem o primeiro nome;

nome = input('qual é o seu nome? ').strip()

# nome = 'Júnior Sousa'

print('seu nome tem:')
print(len(nome), 'letras')

print('seu nome com todas as letras maiusculas é:')
print(nome.upper())

print('seu nome com todas as letras minusculas é: ')
print(nome.lower())

print('seu nome com todas as letras, sem contar os espaços: ')
print(len(nome) - nome.count(' '))

# print('seu primeiro nome tem {} letras.'.format(nome.find(' '))
separa = nome.split()    
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))