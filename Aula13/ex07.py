s = 0
for i in range(1,500,2):
    if i % 3 == 0:
        s += i
print(f'A soma dos valores impares divisíveis por 3 são: {s}')