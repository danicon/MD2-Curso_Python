peso = float(input('Qual é o seu peso? (m) '))
altura = float(input('Qual é a sua altura? (Kg) '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}. Está abaixo do peso!')
elif imc < 25:
    print(f'Seu IMC é de {imc:.2f}. Peso ideal!')
elif imc <= 30:
    print(f'Seu IMC é de {imc:.2f}. Sobrepeso!')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.2f}. Obesidade!')
else:
    print(f'Seu IMC é de {imc:.2f}. Obesidade mórbita!')