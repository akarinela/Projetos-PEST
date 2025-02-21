# Escreva um programa para verificar se um número n de três dígitos é um palíndromo. Ex: 101, 111, ... OBS: NÃO converta N para string. Trate-o como número!

num = int(input('Digite um número: '))

num1 = num%10
num2 = num//10%10
num3 = num//100%10

if num1 == num3:
    print(f'O número: {num} é palíndromo')
else:
    print(f'O número: {num} não é palíndromo')