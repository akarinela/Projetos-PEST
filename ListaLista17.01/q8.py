# Crie uma lista de números inteiros. Em seguida, pergunte ao usuário por um número. Se o número estiver na lista, modifique-o para zero; caso contrário, exiba uma mensagem informando que
#  o número não está na lista.

lista = [99, 98, 100, 105, 200, 347, -2, 45]

numero = int(input("Digite um número: "))

if numero in lista:
    index = lista.index(numero)
    lista[index] = 0
    print(f"Número modificado para zero; Nova lista: {lista}")
else:
    print("O número não está na lista")