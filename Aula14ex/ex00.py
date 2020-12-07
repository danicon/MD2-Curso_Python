sexo = str(input('Digite o seu sexo: ')).strip().upper()
while sexo not in 'FEMININOMASCULINO':
    sexo = str(input('Sexo invalido. Digite o seu sexo novamente: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')