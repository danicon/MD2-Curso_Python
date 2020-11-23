s = 0
cont = 0
for p in range(0,6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s += num
        cont += 1
print(f'A soma dos {cont} números PARES são: {s}')