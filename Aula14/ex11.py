cont = 0
soma = 0
x = 0
while x != 999:
    x = int(input('Digite um número: '))
    soma += x
    cont += 1
    
print(f'Quantidade de números digitados {cont}')
print(f'A soma dos valores são {soma}')