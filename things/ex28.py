# escreva um programa que faça seu PC pensar em um numero inteiro entre 0 e 5 --
# e peça para o usuario tentar descobrir:
# qual foi o numero escolhido pelo computador.
# o programa devera escrever na tela se o usuario VENCEU ou PERDEU

import random
from time import sleep


a = float(input('qual o numero escolhido pelo computador? '))


num = random.choice([1, 2, 3, 4, 5]) # eu poderia usar o randint e colocar o valor entre (0, 5). mas deu na mesma.

print('\033[2;33mPROCESSANDO...\033[m')
sleep(1.5)
print('\033[2;33m-=-\033[m' * 20)
print('\033[2;33mo computador escolheu o numero {}, então...\033[m'.format(num))
print('\033[2;33m-=-\033[m' * 20)


if a == num:
    print('\033[2;34mVOCÊ GANHOU! parabéns, você acertou e ganhou da máquina!\033[m')
else:
    print('\033[2;31mVOCÊ PERDEU! 01001010101\033[m') 