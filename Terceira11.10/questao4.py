# Escreva um programa em Python para somar três números inteiros do usuário. No entanto, se dois valores forem iguais, a soma será zero.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

soma = n1 + n2 + n3

if n1 == n2 or n2 == n3 or n3 == n1:
    soma = 0
    print(f'{soma}')
else:
    print(f'{soma}')