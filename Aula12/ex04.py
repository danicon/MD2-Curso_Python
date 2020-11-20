from datetime import date 

nasc = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - nasc

alis = idade - 18
data = ano + alis

if idade < 18:
    alis = 18 - idade
    data = ano + alis
    print(f'Você tem {idade} anos em {ano}!')
    print(f'Ainda falta {alis} anos para o alistamento')
    print(f'Seu alistamento será em {data}')
elif idade == 18:
    print(f'Você tem {idade} anos em {ano}')
    print('Tem que se alistar imediatamente!')
else:
    alis = idade - 18
    data = ano - alis
    print(f'Você tem {idade} anos em {ano}!')
    print(f'Já deveria ter se alistado há {alis} anos')
    print(f'Seu alistamento foi em {data}')