from random import randint

pc = randint(0,10)
joga = int(input('Tente adivinhar o número que eu escolhi: '))
cont = 1

while joga != pc:
    if joga < pc:
        joga = int(input('Mais! Tente novamente: '))
    if joga > pc:
        joga = int(input('Menos! Tentenovamente: '))
    cont += 1
print(f'PARABÉNS! Você tentou {cont} vezes para acertar.')