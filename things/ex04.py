# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo.
# também exibir todas as informações possíveis sobre ele.

tipo_primitivo = input('digite algo: ')

print('o tipo primitivo é: ', type(tipo_primitivo)) 
print('só tem espaços? ', tipo_primitivo.isspace())
print('é um número? ', tipo_primitivo.isnumeric())
print('é alfabético? ', tipo_primitivo.isalpha())
print('é alfanumérico? ', tipo_primitivo.isalnum())
print('está em maiúsculas? ', tipo_primitivo.isupper())
print('está em minúsculas? ', tipo_primitivo.islower())
print('está capitalizada?', tipo_primitivo.istitle())