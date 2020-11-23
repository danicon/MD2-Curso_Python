t = int(input('Digite um número: '))
x = 0
for i in range(0,11):
    if t > 0:
        x = i * t
        print(f'{t} x {i} = {x}')