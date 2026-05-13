'''
Una empresa de streaming quiere analizar el uso de su plataforma.

Se ingresan:

Año
Mes
Cantidad de horas consumidas
Tipo de usuario:
1 = Básico
2 = Premium
3 = Familiar

La carga finaliza cuando el año sea 0.

Validaciones
Mes entre 1 y 12.
Tipo entre 1 y 3.
Horas mayores a 0.

Informar
Total de horas consumidas.
Promedio de horas por tipo de usuario.
Tipo que más consume.
Mes con menor consumo.
Cantidad de errores del operador.
'''
horas_1 = 0
horas_2 = 0
horas_3 = 0
contador_1 = 0
contador_2 = 0
contador_3 = 0
total_horas = 0
mas_consume = 0
menos_consume = 0
errores = 0
menor_mes = 0
mes_1 = 0
mes_2 = 0
mes_3 = 0
mes_4 = 0
mes_5 = 0
mes_6 = 0
mes_7 = 0
mes_8 = 0
mes_9 = 0
mes_10 = 0
mes_11 = 0
mes_12 = 0
numero_mes = 0
año = input('Ingresa el año: ')

while not (año.isdigit()) or int(año) < 0:
    if not (año.isdigit()):
        print('Error. Solo se permiten digitos.')
    else:
        print('Error. El año debe ser mayor a 0.')
    errores += 1
    año = input('Ingresa el año: ')
año = int(año)

while año != 0:
    mes = input('Ingresa el mes: ')
    while not (mes.isdigit()) or (int(mes) < 1 or int(mes) > 12):
        errores += 1
        if not (mes.isdigit()):
            print('Error. El mes deben ser digitos.')
        else:
            print('Error. Los meses son de 1 a 12.')
        mes = input('Ingresa el mes:')
    mes = int(mes)

    cant_horas = input('Ingresa la cantidad de horas: ')
    while not (cant_horas.isdigit()) or int(cant_horas) <= 0:
        errores += 1
        if not (cant_horas.isdigit()):
            print('Error. Solo se permiten digitos')
        else:
            print('Error. La cantidad de horas debe ser mayor a 0.')
        cant_horas = input('Ingresa la cantidad de horas: ')
    cant_horas = int(cant_horas)

    tipo_de_user = input('Ingresa el tipo de usuario (1-3): ')
    while not (tipo_de_user.isdigit()) or (int(tipo_de_user) < 1 or int(tipo_de_user) > 3):
        errores += 1
        if not (tipo_de_user.isdigit()):
            print('Error. Solo se permiten digitos.')
        else:
            print('Error. El rango de usuario debe ir de 1 a 3.')
        tipo_de_user = input('Ingresa el tipo de usuario (1-3):')
    tipo_de_user = int(tipo_de_user)
    
    total_horas += cant_horas

    if tipo_de_user == 1:
        horas_1 += cant_horas
        contador_1 += 1
    elif tipo_de_user == 2:
        contador_2 += 1
        horas_2 += cant_horas
    elif tipo_de_user == 3:
        contador_3 += 1
        horas_3 += cant_horas
    
    if mes == 1:
        mes_1 += cant_horas
    elif mes == 2:
        mes_2 += cant_horas
    elif mes == 3:
        mes_3 += cant_horas
    elif mes == 4:
        mes_4 += cant_horas
    elif mes == 5:
        mes_5 += cant_horas
    elif mes == 6:
        mes_6 += cant_horas
    elif mes == 7:
        mes_7 += cant_horas
    elif mes == 8:
        mes_8 += cant_horas
    elif mes == 9:
        mes_9 += cant_horas
    elif mes == 10:
        mes_10 += cant_horas
    elif mes == 11:
        mes_11 += cant_horas
    elif mes == 12:
        mes_12 += cant_horas    
    
    menor_mes = mes_1
    numero_mes = 1
    if mes_2 < menor_mes:
        menor_mes = mes_2
        numero_mes = 2
    if mes_3 < menor_mes:
        menor_mes = mes_3
        numero_mes = 3
    if mes_4 < menor_mes:
        menor_mes = mes_4
        numero_mes = 4
    if mes_5 < menor_mes:
        menor_mes = mes_5
        numero_mes = 5
    if mes_6 < menor_mes:
        menor_mes = mes_6
        numero_mes = 6
    if mes_7 < menor_mes:
        menor_mes = mes_7
        numero_mes = 7
    if mes_8 < menor_mes:
        menor_mes = mes_8
        numero_mes = 8
    if mes_9 < menor_mes:
        menor_mes = mes_9
        numero_mes = 9
    if mes_10 < menor_mes:
        menor_mes = mes_10
        numero_mes = 10
    if mes_11 < menor_mes:
        menor_mes = mes_11        
        numero_mes = 11
    if mes_12 < menor_mes:
        menor_mes = mes_12
        numero_mes = 12
    
    año = input('Ingresa el año: ')

    while not(año.isdigit()) or int(año) < 0:
        if not(año.isdigit()):
            print('Error. Solo se permiten digitos.')
        else:
            print('Error. El año debe ser mayor o igual a 0.')
        errores += 1
        año = input('Ingresa el año: ')
    año = int(año)

if contador_1 > 0:
    prom_1 = horas_1 / contador_1
else:
    prom_1 = 0
if contador_2 > 0:
    prom_2 = horas_2 / contador_2
else:
    prom_2 = 0
if contador_3 > 0:
    prom_3 = horas_3 / contador_3
else:
    prom_3 = 0
    
if prom_1 > prom_2 and prom_1 > prom_3:
    mas_consume = 'Tipo 1'
elif prom_2 > prom_3:
    mas_consume = 'Tipo 2'
else:
    mas_consume = 'Tipo 3'
        
if prom_1 < prom_2 and prom_1 < prom_3:
    menos_consume = 'Tipo 1'
elif prom_2 < prom_3:
    menos_consume = 'Tipo 2'
else:
    menos_consume = 'Tipo 3'
    
print(f'El total de horas consumidas es de {total_horas} hs')
print(f'El promedio de horas para el tipo 1 es: {prom_1}')
print(f'El promedio de horas para el tipo 2 es: {prom_2}')
print(f'El promedio de horas para el tipo 3 es: {prom_3}')
print(f'El tipo que mas consume es {mas_consume}')
print(f'El tipo que menos consume es {menos_consume}')
print(f'El mes con la menor cantidad es {numero_mes}')
print(f'La cantidad de errores es de {errores}')