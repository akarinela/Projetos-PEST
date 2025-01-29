#Crie uma lista de nomes de cidades e peça ao usuário para digitar o nome de uma cidade. 
# O programa deve verificar se a cidade existe na lista usando a operação in e informar ao usuário se a cidade existe ou não.

cidades = ["sobral",'pernambuco','maranguape',"são paulo",'natal','maranhão',"ibicutinga",'iguatu']
print(cidades)

nome = input("digite um nome de uma cidade: ")

if nome in cidades:
    print(f'A cidade {nome} está na lista.')
else:
    print(f'A cidade {nome} não está na lista')