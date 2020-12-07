from random import randint
print(30*'=-')
print('VAMOS JOGAR PAR OU ÍMPAR')
print(30*'=-')
cont = 0
while True:
    jogn =  int(input('Diga um valor: '))
    jogpi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()

    pcn = randint(0, 10)
    soma = jogn + pcn 
    if soma % 2 == 0:
        pi = 'PAR'
    else:
        pi = 'IMPAR'

    if jogpi == 'P'and soma % 2 == 0:
        res = 'VOCÊ VENCEU!'
    elif jogpi == 'I' and soma % 2 != 0:
        res = 'VOCÊ VENCEU!'
    else:
        res = 'VOCÊ PERDEU!'
    print(30*'-')
    print(f'Você jogou {jogn} e o computador {pcn}. Total deu {soma} DEU {pi}')
    print(30*'-')
    print(res)

    if res == 'VOCÊ PERDEU!':
        break
    print('Vamos jogar novamente...')
    print(30*'=-')
    cont += 1

print(30*'=-')
print(f'GAME OVER! Você venceu {cont} vezes.')
print(30*'=-')