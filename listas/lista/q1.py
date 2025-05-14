# Dada a lista lista = [20, 76, 94, 60, 28, 65, 4, 69, 71, 22] responda qual sub-lista é gerada após cada código a seguir:
# i) lista[3:8]
# lista[3:-3]
# lista[2::2]
# lista[2:-2:2]
# lista[-1:0]
# lista[-1:0:-1]
# lista[-1::-1]
# lista[::-1]
# lista[6::-2]

lista = [20, 76, 94, 60, 28, 65, 4, 69, 71, 22]

print(lista[3:8])
# [60, 28, 65, 4, 69]
print(lista[3:-3])
# [60, 28, 65, 4]
print(lista[2::2])
# [94, 28, 4, 71]
print(lista[2:-2:2])
# [94, 28, 4]
print(lista[-1:0])
# []
print(lista[-1:0:-1])
# [22, 71, 69, 4, 65, 28, 60, 94, 76]
print(lista[-1::-1])
# [22, 71, 69, 4, 65, 28, 60, 94, 76, 20]
print(lista[::-1])
# [22, 71, 69, 4, 65, 28, 60, 94, 76, 20]
print(lista[6::-2])
# [4, 28, 76]