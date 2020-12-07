print(20*'-')
print('LOJA SUPER BARATÃO')
print(20*'-')
soma = p = cont = menor = 0
while True:
    prdnome = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    conti = str(input('Quer continuar? [S/N] ')).strip().upper()
    while conti != 'S' and conti != 'N':
        conti = str(input('Quer continuar? [S/N] ')).strip().upper()
    soma += preco
    if preco > 1000:
        p += 1
    if cont == 0:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            nome = prdnome
    if conti == 'N':
        break
    cont += 1

print(7*'-','FIM DO PROGRAMA',7*'-')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {p} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custa R${menor:.2f}')