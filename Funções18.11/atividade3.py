# Crie 4 funções diferentes. Cada função irá receber 2 parâmetros e irá retornar um cálculo.
# As4 funções são:
# - Somar (num1, num2): deve retornar a soma de num1 com num2.
# - Subtrair (num1, num2): deve retornar a subtrair de num1 por num2.
# - Multiplicar (num1, num2): deve retornar a multiplicar de num1 por num2.
# - Dividr (num1, num2): deve retornar a dividir de num1 por num2.

def soma(num1: float, num2: float):
    resul = num1 + num2
    return resul

def subtrair(num1: float, num2: float):
    resul = num1 - num2
    return resul

def multiplicar(num1: float, num2: float):
    resul = num1 * num2
    return resul

def dividir(num1: float, num2: float):
    resul = num1 / num2
    return resul

valorsoma = soma(5, 5)
print(f'A soma dos números é: {valorsoma}')

valorsubtrair = subtrair(5, 5)
print(f'A subtração dos números é: {valorsubtrair}')

valormultiplicar = multiplicar(5, 5)
print(f'A multiplicação dos números é: {valormultiplicar}')

valordividir = dividir(5, 5)
print(f'A divisão dos números é: {valordividir}')