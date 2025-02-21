# Crie um código em Python que solicite ao usuário um número e, usando o comando "while", 
# imprima todos os divisores desse número até que o usuário digite "0" para encerrar o programa

numero = int(input('Digite um número: '))
contador = 1

while contador <= numero:
    if numero % contador == 0:
        print(contador)
    contador += 1