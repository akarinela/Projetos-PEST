# Escreva um programa para calcular a soma dos dígitos de um número de 4 dígitos.
# Ex: para N = 5928, mostre: 24

num = int(input('Digite um número de quatro dígitos: '))

cal = num%10
cal2 = num//10%10
cal3 = num//100%10
cal4 = num//1000%10

soma = cal + cal2 + cal3 + cal4

print(f'{soma}')