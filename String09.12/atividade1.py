# Escreva uma função em Python chamada primeiro_e_ultimo que receba uma string como entrada e retorne um nova string contendo apenas o primeiro e o último caractere da string original

def primeiro_e_ultimo(nome: str):
    primeiro = nome[0]
    ultimo = nome[len(nome) -1]
    novastring = primeiro + ultimo
    return novastring

resultado = primeiro_e_ultimo("Karine")
print(resultado)