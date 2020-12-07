while True:
    print(30*'-')
    t = int(input('Quer ver a tabuada de qual valor? '))
    print(30*'-')
    c = 1
    m = 1
    if t < 0:
        break
    while c <= 10:
        m = t * c 
        print(f'{t} x {c} = {m}')
        c += 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')