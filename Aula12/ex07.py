num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
num3 = float(input('Digite o terceiro valor: '))

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    if num1 == num2 and num2 == num3:
        print('EQUILÁTERO - Todos os lados são iguais!')
    elif num1 == num2 or num2 == num3 or num1 == num3:
        print('ISÓSCELES - Dois lados iguai!')
    else:
        print('ESCALENO - Todos os lados são diferentes!')
else:
    print('Não pode formar um triângulo!')
