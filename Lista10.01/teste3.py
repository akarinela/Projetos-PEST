n1 = float(input('Digite um nota: '))
n2 = float(input('Digite um nota: '))
n3 = float(input('Digite um nota: '))
n4 = float(input('Digite um nota: '))
n5 = float(input('Digite um nota: '))
n6 = float(input('Digite um nota: '))
n7 = float(input('Digite um nota: '))

notas = [6, 7, 5, 8, 9]
quantidade = len(notas)

soma = 0

for i in range(quantidade):
    soma += notas[i]
    
media = soma / quantidade
print(media)