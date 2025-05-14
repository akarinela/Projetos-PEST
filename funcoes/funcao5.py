# Crie um função que receba dois números e escreva na tela quem é o maior e quem é o menor número. Caso seja iguais, escreva 'são iguais´.

def maior(numero1, numero2):
    if numero1 > numero2:
        print(f'O número {numero1} é maior que o número {numero2}')
    elif numero2 > numero1:
        print(f'O número {numero2} é maior que o número {numero1}')
    elif numero1 == numero2:
        print('Os números são iguais')

maior(10, 10)