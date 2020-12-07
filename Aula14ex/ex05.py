primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= mais:
        print(f'{termo} \032 ', end='')
        termo += razao
        cont += 1
    print('Pausa...')
    mais = int(input('Mais quantos? '))
print(f'Progressão finalizada com {total} termos mostrados.')
