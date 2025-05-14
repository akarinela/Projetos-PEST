notas = [6, 7, 5, 8, 9]
quantidade = len(notas)

soma = 0

for i in range(quantidade):
    notas[i] = int(input('Digite uma nota: '))
    soma += notas[i]
    
media = soma / quantidade
print(media)