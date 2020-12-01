from time import sleep
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print()
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa''')
    print()
    opcao = int(input('>>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os número novamente:')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print(10*'=-=')
    sleep(1)
print('Fim do programa! Volte sempre!')