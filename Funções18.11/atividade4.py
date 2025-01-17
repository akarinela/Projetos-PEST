# Crie uma função que receba dois números e retorno e maior deles.

def maior(numero1, numero2):
    if numero1 > numero2:
        maior = numero1
    elif numero2 > numero1:
        maior = numero2
    else:
        maior == numero1
    return maior

print(maior(10, 20))