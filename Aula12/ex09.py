valor = float(input('Qual é o preço do produto? R$'))
print()
print(6*'=','CONDIÇÕES DO PAGAMENTO',6*'=')
print()
print('1 - Á vista dinheiro/cheque: 10% de desconto')
print('2 - Á vista no cartão: 5% de desconto')
print('3 - Em até 2x no cartão: preço normal')
print('4 - 3x ou mais no cartão: 20% de juros')
print()
cond = int(input('Qual é a opção? '))

if cond == 1:
    preco = valor - ((valor * 10) / 100)
elif cond == 2:
    preco = valor - ((valor * 5) / 100)
elif cond == 3:
    preco = valor
elif cond == 4:
    parcela = int(input('Quanta parcelas? '))
    preco = valor * 1.20
    parc = preco / parcela
    print(f'Sua compra será parcela em 10x de R${parc:.2f} COM JUROS')
else:
    print('Condição inválida. Tente novamente!')

print(f'O valor total: R${preco:.2f}')