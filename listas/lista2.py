frutas = ["maçã","uva","laraja","limão"]


print(f"lista de frutas atual:{frutas}")
fruta = input("digite uma fruta:")


if fruta in frutas:
    frutas.remove(fruta)
    print(f"fruta removida.lista resultante {frutas}")
else:
    print("nenhuma alteração feita")