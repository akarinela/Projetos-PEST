notas = [6, 7, 5, 8, 9]

quantidade = len(notas)

soma = 0
for i in range(quantidade):
    soma = soma + notas[i]
    
media = soma/quantidade
print(f'Média = {media}')