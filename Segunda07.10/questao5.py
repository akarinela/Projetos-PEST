# Escreva um programa para ler um número N e mostre N, NN e NNN.
# OBS: NÃO converta N para string. Trate-o como número!
# Ex: para N = 5, mostre: 5, 55, 555

numero = int(input('Digite um número: '))

dezena = (numero * 10) + numero
centena = (numero * 111) 

print (f' {numero} {dezena} {centena}') 