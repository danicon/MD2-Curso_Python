c = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
while c == 'S':
    num = int(input('Digite um número: '))
    soma += num
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num 
    c = str(input('Deseja continuar? ')).strip().upper()[0]
    cont += 1
print(f'A media é de {soma / cont}, o maior número é {maior} e o menor é {menor}')