#Escreva um programa para converter distância de metros para pés, polegadas e milhas.

metros = int(input('Digite um número: '))

pes = metros * 3.28084

polegdas = metros * 39.3701

milhas = metros * 0.000621371

print(f'metros para pés: {pes} metros para polegadas: {polegdas} metros para milhas: {milhas}')