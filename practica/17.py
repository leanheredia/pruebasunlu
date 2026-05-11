'''
Se realizó una encuesta a 2500 personas.

Se pide ingresar:

Edad
Horas semanales de juego
Rangos
10 a 17
18 a 30
31 a 50
Más de 50
Pedidos
Informar el promedio de horas por rango.
Mostrar qué rango juega más.
Mostrar qué rango juega menos.
Validar que la edad sea positiva.
Validar que las horas estén entre 0 y 168.
'''
acumulador_10_17 = 0
acumulador_18_30 = 0
acumulador_31_50 = 0
acumulador_mas_50 = 0

contador_personas_10_17 = 0
contador_personas_18_30 = 0
contador_personas_31_50 = 0
contador_personas_mas_50 = 0

for i in range(2500):
    edad = input('Ingresa tu edad: ')
    horas_semanales = input('Ingresa las horas semanales de juego: ')

    while not (edad.isdigit()) or (int(edad) <= 0):
        if not edad.isdigit():
            print('Error. Solo se permiten digitos')
        else:
            print('La edad debe ser mayor a 0.')
        edad = input('Ingresa tu edad: ')
    while not(horas_semanales.isdigit()) or (int(horas_semanales) < 0 or int(horas_semanales) > 168):
        if not(horas_semanales.isdigit()):
            print('Error. Solo se permiten digitos')
        else:
            print('Los valores estan entre 0 y 168')
        horas_semanales = input('Ingresa las horas semanales de juego: ')
    edad = int(edad)
    horas_semanales = int(horas_semanales)
    if edad >= 10 and edad <= 17:
        acumulador_10_17 += horas_semanales
        contador_personas_10_17 += 1
    elif edad >= 18 and edad <= 30:
        acumulador_18_30 += horas_semanales
        contador_personas_18_30 += 1
    elif edad >= 31 and edad <= 50:
        acumulador_31_50 += horas_semanales
        contador_personas_31_50 += 1
    elif edad > 50:
        acumulador_mas_50 += horas_semanales
        contador_personas_mas_50 += 1
if contador_personas_10_17 > 0:
    prom_10_17 = acumulador_10_17 / contador_personas_10_17
else:
    prom_10_17 = 0
if contador_personas_18_30 > 0:
    prom_18_30 = acumulador_18_30 / contador_personas_18_30
else:
    prom_18_30 = 0
if contador_personas_31_50 > 0:
    prom_31_50 = acumulador_31_50 / contador_personas_31_50
else:
    prom_31_50 = 0
if contador_personas_mas_50 > 0:
    prom_mas_50 = acumulador_mas_50 / contador_personas_mas_50
else:
    prom_mas_50 = 0

mayor = prom_10_17
rango_mayor = '10-17'

if prom_18_30 > mayor:
    mayor = prom_18_30
    rango_mayor = '18-30'
if prom_31_50 > mayor:
    mayor = prom_31_50
    rango_mayor = '31-50'
if prom_mas_50 > mayor:
    mayor = prom_mas_50
    rango_mayor = '>50'

menor = prom_10_17 
rango_menor = '10-17'

if prom_18_30 < menor:
    menor = prom_18_30
    rango_menor = '18-30'
if prom_31_50 < menor:
    menor = prom_31_50
    rango_menor = '31-50'
if prom_mas_50 < menor:
    menor = prom_mas_50
    rango_menor = '>50'

print(f'Promedio 10-17: {prom_10_17}')
print(f'Promedio 18-30: {prom_18_30}')
print(f'Promedio 31-50: {prom_31_50}')
print(f'Promedio >50: {prom_mas_50}')

print(f'El rango que mas juega es {rango_mayor}')
print(f'El rango que menos juega es {rango_menor}')