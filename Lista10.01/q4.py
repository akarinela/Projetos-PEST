lista = [1,2,3,4,88,5,6]
copia = lista[:]


for numero in lista:
    if numero % 2 == 0:
        copia.remove(numero)


print(copia)
     
    