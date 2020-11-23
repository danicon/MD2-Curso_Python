media = 0
menor = 0
maior = 0

for g in range(1,5):
    print(5*'-',end='')
    print(f' {g}ª PESSOA ',end='')
    print(5*'-')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    media += idade
    if idade < 20 and sexo == 'F':
        menor += 1
    if g == 1 and sexo == 'M':
        maior = idade
        nom = nome
    else:
        if idade > maior and sexo == 'M':
            maior = idade
            nom = nome

print(f'\nA média de idade do grupo é {media/4} anos')
print(f'O {nom} com {maior} anos é o mais velho')
print(f'Quantidade de mulheres com menos de 20 anos é {menor}')