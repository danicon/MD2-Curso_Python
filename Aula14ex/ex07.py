num = int(input('Digite um valor: [999 para finalizar] '))
soma = 0
cont = 0
while num != 999:
    soma += num
    num = int(input('Digite um valor: [999 para finalizar] '))  
    cont += 1
print(f'A soma dos {cont} é {soma}') 