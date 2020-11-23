from datetime import date

ano = date.today().year
menor = 0
maior = 0
for nas in range(0,7):
    nascimento = int(input(f'Em que ano a {nas+1}ª pessoa nasceu? '))
    nasc = ano - nascimento 
    if nasc < 21:
        menor += 1
    else:
        maior +=1
print(f'\nAo todo tivemos {maior} pessoas maiores de idade')
print(f'Ao todo tivemos {menor} pessoas menores de idade')