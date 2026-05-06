#tabla de multiplicar del 2 hasta el 6

for i in range(2, 6):
    print('Tabla de', i)
    for k in range(1, 11):
        resultado = i * k
        print(f'{i} * {k} = {resultado}')
    print()