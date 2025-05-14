# Crie uma função chamada converter_moeda que aceita um valor em reais e um parâmetro nomeado para_dolar (com valor padrão True). Se para_dolar for True, a função deve converter o valor
#  para dólares (usando uma taxa fictícia) e retornar o valor convertido. Caso contrário, deve retornar o valor original em reais.

def converter_moeda(para_dolar = True):
    taxa = 5.81
    if para_dolar == True:
        dolar = num / taxa
        return dolar
    else:
        return num

num = int(input("Digite um valor: "))

resul = converter_moeda()

print(resul)