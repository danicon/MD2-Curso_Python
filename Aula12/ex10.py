from time import sleep
import random

print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')  
joga = int(input('Qual é a sua jogada? '))
pc = random.randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

if joga == 0 and pc == 2:
    res = 'JOGADOR VENCE'
elif pc == 0 and joga == 2:
    res = 'COMPUTADOR VENCEU'
elif joga > pc:
    res = 'JOGADOR VENCE'
elif joga == pc:
    res = 'IMPATE'
else:
    res = 'COMPUTADOR VENCEU'
    

print(10*'-=-')

if joga == 0:
    simbolo = 'Pedra'
elif joga == 1:
    simbolo = 'Papel'
elif joga == 2:
    simbolo = 'Tesoura'

if pc == 0:
    simb = 'Pedra'
elif pc == 1:
    simb = 'Papel'
elif pc == 2:
    simb = 'Tesoura'

print(f'Computador jogou {simb}')
print(f'Jogador jogou {simbolo}')
print(10*'-=-')
print(res)