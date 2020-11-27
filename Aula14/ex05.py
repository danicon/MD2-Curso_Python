import random

pc = random.randint(0,10)
jg = 0
tent = 0
while jg != pc:
    jg = int(input('Adivinhe o número da computador: '))
    tent += 1
    if jg != pc:
        print('Você errou!')
print('Parabéns! Você acertou!')
print(f'Precisou de {tent} tentavida para acertar!')
print(pc)