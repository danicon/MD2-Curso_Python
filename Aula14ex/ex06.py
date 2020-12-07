n = int(input('Digite um numero: '))
f = n
num1 = 0
num2 = 1
cont = 3
print(f'{num1} -> {num2} -> ', end='')
while cont <= f:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    cont += 1
    print(f'{num3} -> ', end='')
print('FIM')