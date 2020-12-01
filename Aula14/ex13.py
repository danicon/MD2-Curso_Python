n = int(input('Digite um número: '))
f = 1
print(f'Calculando {n}! = ', end='')
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)