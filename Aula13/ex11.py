num = int(input('Digite um número: '))
tot = 0

for p in range(1, num+1):
    if num % p == 0:
        tot += 1
    print(f'{p}', end=' ')
print(f'\nO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')