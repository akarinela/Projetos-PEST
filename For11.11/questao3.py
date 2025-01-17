# Crie um programa em Python que imprima a soma dos números pares de 0 até um número inteiro dado pelo usuário. Utilize o comando for para percorrer os números e realizar a soma.

numero = int(input('Digite um número: '))

soma = 0

for n in range(numero+1):
    if n %2 == 0:
        soma += n
    
print(soma)