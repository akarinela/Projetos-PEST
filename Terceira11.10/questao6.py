# Crie um programa para ler um número de 5 dígitos e verificar se existe algum dígito que se repete 2 ou mais vezes. OBS: NÃO converta N para string. Trate-o como número!

num = int(input('Digite um número de 5 dígitos: '))

num1 = num%10
num2 = num//10%10
num3 = num//100%10
num4 = num//1000%10
num5 = num//10000%10

soma = num1 + num2 + num3 + num4 + num5

print(f'{soma}')