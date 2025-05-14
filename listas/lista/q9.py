# Crie uma lista vazia com cinco posições e, em seguida, peça ao usuário para inserir cinco nomes. Armazene esses nomes na lista e, por fim, exiba a lista completa.

nomes = [None] * 5

for i in range(5):
    nomes[i] = input(f"Digite o {i + 1} nome: ")

# Exibe a lista completa
print("Lista completa de nomes: ")
print(nomes)
