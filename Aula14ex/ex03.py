num = int(input('Digite um número: '))
c = num
f = 1
print(f'fatotial de {num}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)