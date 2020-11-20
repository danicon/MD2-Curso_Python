num = int(input('Digite um número para conversão: '))
print()
print('1 - para binário')
print('2 - para octal')
print('3 - para hexadecimal')
print()
opcao = int(input('Escolha o tipo de conversão: '))

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}') 
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente!')