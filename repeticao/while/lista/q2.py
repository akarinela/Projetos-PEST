# Crie um código em Python que peça ao usuário para digitar um número inteiro positivo, e então utilize o comando "while" para imprimir cada número até chegar ao número digitado pelo usuário.

numero = int(input('Digite um número inteiro positivo: '))

controladora = 1
while controladora <= numero:
    print(controladora)
    controladora += 1