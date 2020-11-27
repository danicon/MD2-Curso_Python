num = float(input('Digite o primeiro valor: '))
num1 = float(input('Digite o segundo valor: '))
print()
print('[1]Somar')
print('[2]Multiplicar')
print('[3]Maior')
print('[4]Novos números')
print('[5]Sair do programa')
print()

c = 1
while c > 0 and c < 5:
    c = int(input('Escolha uma opção: '))
    if c == 1:
        s = num + num1
        print(f'Resultado da Soma: {s}')
    if c == 2:
        m = num * num1
        print(f'Resultado da Multiplicação: {m}')
    if c == 3:
        maior = num
        if maior < num1:
            maior = num1
        print(f'O Maior número é: {maior}')
    if c == 4:
        num = float(input('Digite o primeiro valor: '))
        num1 = float(input('Digite o segundo valor: '))
print('Até breve ;)')
