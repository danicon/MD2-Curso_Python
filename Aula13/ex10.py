print(20*'=')
print('10 TERMOS DE UMA PA')
print(20*'=')
prim = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = prim + (10 - 1) * razao

for p in range(prim, decimo + razao, razao):
    print(p,end = ' \032 ')
print('ACABOU')
