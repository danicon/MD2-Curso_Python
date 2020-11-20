casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = float(input('Em quanto você vai pagar a casa? '))
emprestimo = casa / (anos * 12)
parcela = (salario * 30) / 100

if emprestimo > parcela:
    print(f'Infelizmente o emprestimo de R${emprestimo:.2f} excedeu os 30% do seu salário')
else:
    print(f'Você vai pagar o emprestimo mensalmente no valor de R${emprestimo:.2f}')