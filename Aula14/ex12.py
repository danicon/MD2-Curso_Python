v = 'S'
cont = 0
while v == 'S':
    num =  int(input('Digite um número: '))
    v = str(input('Quer contnuar? [S/N] ')).upper()
    maior = 0
    menor = num
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    num += num
    cont += 1
    if v == 'N':
        print('FIM!') 
print(f'A média é de {num / cont}')
print(f'{maior} é o maior')
print(f'{menor} é o menor')