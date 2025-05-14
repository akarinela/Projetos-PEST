# Crie uma função que receba dois parâmetros: A altura e a largura de um retângulo. Sua função deve calcular e RETORNAR a área desse retângulo.

def calculo_area_retangulo(altura: int, largura: int):
    area = altura * largura
    return area

var = calculo_area_retangulo(2, 5)
print(f'Área: {var}')