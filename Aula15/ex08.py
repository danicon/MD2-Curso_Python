print(30*'=')
print('BANCO CEV')
print(30*'=')
cinq = vinte = dez = um = 0
sacar = int(input('Que valor você quer sacar? R$'))
while sacar >= 50:
    sacar -= 50
    cinq += 1 
while sacar >= 20:
    sacar -= 20
    vinte += 1
while sacar >= 10:
    sacar -= 10
    dez += 1
while sacar >= 1:
    sacar -= 1
    um += 1
print(f'Total de {cinq} cédulas de R$50')
print(f'Total de {vinte} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {um} cédulas de R$1')
print(30*'=')
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')