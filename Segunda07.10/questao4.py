# Escreva um programa em Python que resolve a versão geral do problema acima. Peça ao usuário que entre com a hora atual (em horas) e que entre com o número de horas que 
# deverá esperar antes do alarme tocar. Seu programa deve imprimir a hora que o alarme irá tocar.

hora = int(input('Escolha uma hora: '))
alarme = int(input('Escolha um horario para o alarme tocar: '))

hora_final = (hora + alarme) % 24

print(f'O alarme irá tocar às {hora_final}h')