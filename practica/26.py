errores = 0

año = int(input('Ingrese el año: '))
while año != 0:
    mes = input('Ingrese el mes: ')

    while not mes.isdigit() or (int(mes) < 1 or int(mes) > 12):
        errores = errores + 1
        if not mes.isdigit():
            print('Error. Solo se permiten digitos.')
        else:
            print('Error. Fuera de rango. Solo permite (1-12)')
        mes = input('Ingrese el mes: ')
    mes = int(mes)

    cantidad_autos_vendidos = int(input('Ingresa la cantidad de autos vendidos: '))
    año = int(input('Ingrese el año: '))

print('La cantidad de errores fue de', errores)
