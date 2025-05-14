# 5. Crie uma lista de nomes de frutas. Em seguida, peça ao usuário para inserir o nome de uma fruta e verifique se essa fruta está na lista. Exiba uma mensagem informando se a fruta 
# está ou não na lista.

frutas = ['uva','banana','abacaxi','laranja','limão']

nomefruta = input("Digite o nome de uma fruta: ")

tamanho = len(frutas)

contador = 0

while contador < tamanho:
    if frutas[contador] == nomefruta:
         print(f"A fruta {nomefruta} está na lista")
    contador = contador + 1