ida = hosx = musx = 0

while True:
    print(20*'-')
    print(f'{"CADASTRE UMA PESSOA":^20}')
    print(20*'-')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    print(20*'-')
    conti = str(input('Quer continuar? [S/N] ')).strip().upper()
    while conti != 'S' and conti != 'N': 
        conti = str(input('Quer continuar? [S/N] ')).strip().upper()
    if idade > 18:
        ida += 1
    if sexo == 'M':
        hosx += 1
    if sexo == 'F' and idade < 20:
        musx += 1
    if conti == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {ida}')
print(f'Ao todo temos {hosx} homens cadastrados')
print(f'E temos {musx} mulheres com menos de 20 anos')