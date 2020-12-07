n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
opcao = 0
while opcao != 5:
    print()
    print('''        [1]Somar
        [2]Multiplicar
        [3]Maior
        [4]Novos números
        [5]Sair do programa''')
    print()
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'{n1} x {n2} = {mult}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor é {maior}') 
    elif opcao == 4:
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print(10*'=-=')

print('Fim do programa! Volte sempre!')