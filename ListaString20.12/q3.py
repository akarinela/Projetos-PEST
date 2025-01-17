# Reverter String
# Enunciado: Crie uma função chamada reverter que receba uma palavra e devolva a palavra de trás para frente.
# Exemplo:
# Entrada: "Python"
# Saída: "nohtyP"

def reverter(string : str):
    stringinvertida = ''

    for i in range(-1, -len(string)-1, -1):
        print(f"Índice: {i} :: {string[i]}")
        stringinvertida = stringinvertida + string[i]

    return stringinvertida

print(reverter("Python"))