num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
media = (num1 + num2) / 2
print(f'Sua média foi de {media:.1f}')

if media < 5:
    print('REPROVADO!')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')