s = 'M'
while s == 'M' or s == 'F':
    s = str(input('Sexo [M/F]: ')).upper()
    print(f'Seu sexo é {s}')
print('Valor informado não é valido. Digite novamente!')


