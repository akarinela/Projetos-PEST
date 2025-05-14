lista = []

while True:
    numero = int(input("digite um numero(digite 0 para sair):"))
    if numero != 0:
        lista.append(numero)
    else:
        break
print(lista)