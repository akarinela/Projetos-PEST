# Crie uma função chamada calculadora que aceita três parâmetros: num1, num2 e operacao. A operação pode ser "soma", "subtracao", "multiplicacao" ou "divisao". A função deve retornar 
# o resultado da operação.

operacao = input('Digite uma operação: ')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))


def calculadora(num1: int, num2: int, operacao: str):
    if operacao == 'soma':
        resultado = num1 + num2
    elif operacao == 'subtracao':
        resultado= num1 - num2
    elif operacao == 'multiplicacao':
        resultado = num1 * num2
    elif operacao == 'duvisao':
        resultado = num1 / num2
    else:
        print('Operação inválida')
    return resultado

resultado = calculadora(num1, num2, operacao)

print(f'O resultado é igual a: {resultado}')