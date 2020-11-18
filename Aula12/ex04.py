from datetime import date 

nasc = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - nasc

if idade < 18:
    print(f'Você tem {idade}, aida vai se alistar!')
elif idade == 18:
    print(f'Você tem {idade}, hora de se alistar!')
else:
    print(f'Você tem {idade}, passou do tempo do alistamento!')