casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = float(input('Em quanto você vai pagar a casa? '))
emprestimo = casa / anos
parcela = (salario * 30) / 100

if emprestimo > parcela:
    print(f'Infelizmente o emprestimo de R${emprestimo} excedeu os 30% do seu salário R${parcela}')
else:
    print(f'Você vai pagar o emprestimo mensalmente no valor de R${emprestimo}')