print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termo você quer? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} \032 {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' \032 {t3}', end='')
    t1 = t2
    t2 = t3
    cont+=1
print(' \032 FIM')
print('~'*30)