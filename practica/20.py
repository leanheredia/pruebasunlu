'''
Ejercicio 6 — Difícil con acumuladores y contadores

Una facultad quiere registrar notas de estudiantes.

Ingresar:

Carrera
1 = Sistemas
2 = Industrial
3 = Civil
Nota final
Edad

La carga termina cuando la carrera sea 0.

Validaciones
Carrera entre 1 y 3.
Nota entre 1 y 10.
Edad mayor a 16.

Informar
Promedio de notas por carrera.
Carrera con mejor promedio.
Cantidad de alumnos desaprobados.
Promedio general.
Total de errores.
'''
#Validaciones

notas_carrera_1 = 0
notas_carrera_2 = 0
notas_carrera_3 = 0
alumnos_carrera_1 = 0
alumnos_carrera_2 = 0
alumnos_carrera_3 = 0
total_alumnos = 0
total_notas = 0
errores = 0
alumnos_desaprobados = 0


carrera = input('Elige una carrera (1-3), 0 para terminar: ')

while not (carrera.isdigit()) or (int(carrera) < 0 or int(carrera) > 3):
    errores += 1
    if not (carrera.isdigit()):
        print('Deben ser numeros.')
    else:
        print('Deben ser numeros del 1 al 3.')
    carrera = input('Elige una carrera (1-3), 0 para terminar: ')
carrera = int(carrera)

while carrera != 0:
    nota_final = input('Ingresa la nota final del alumno (1-10): ')
    while not (nota_final.isdigit()) or (int(nota_final) < 1 or int(nota_final) > 10):
        errores += 1
        if not (nota_final.isdigit()):
            print('Deben ser numeros.')
        else:
            print('Deben ser numeros del 1 al 10.')
        nota_final = input('Ingresa la nota final del alumno (1-10): ')
    nota_final = int(nota_final)

    edad = input('Ingresa la edad del alumno: ')
    while not (edad.isdigit()) or (int(edad) < 16):
        errores += 1
        if not edad.isdigit():
            print('Error. La edad debe ser digitos.')
        else:
            print('Error. La edad debe ser >16.')
        edad = input('Ingresa la edad del alumno: ')
    edad = int(edad)
    #Calculos para carrera
    total_notas += nota_final
    if carrera == 1:
        notas_carrera_1 += nota_final
        alumnos_carrera_1 += 1
        if nota_final < 4:
            alumnos_desaprobados += 1
        total_alumnos += 1
    
    elif carrera == 2:
        notas_carrera_2 += nota_final
        alumnos_carrera_2 += 1
        if nota_final < 4:
            alumnos_desaprobados += 1
        total_alumnos += 1

    elif carrera == 3:
        notas_carrera_3 += nota_final
        alumnos_carrera_3 += 1
        if nota_final < 4:
            alumnos_desaprobados += 1
        total_alumnos += 1
    carrera = input('Elige una carrera (1-3), 0 para terminar: ')
    while not (carrera.isdigit()) or (int(carrera) < 0 or int(carrera) > 3):
        errores += 1
        if not (carrera.isdigit()):
            print('Deben ser numeros.')
        else:
            print('Deben ser numeros del 1 al 3.')
        carrera = input('Elige una carrera (1-3), 0 para terminar: ')
    carrera = int(carrera)
#Calculos para promedio

if alumnos_carrera_1 > 0:
    prom_1 = notas_carrera_1 / alumnos_carrera_1
else:
    prom_1 = 0
if alumnos_carrera_2 > 0:
    prom_2 = notas_carrera_2 / alumnos_carrera_2
else:
    prom_2 = 0
if alumnos_carrera_3 > 0:
    prom_3 = notas_carrera_3 / alumnos_carrera_3
else:
    prom_3 = 0

#Mayor promedio
if prom_1 > prom_2 and prom_1 > prom_3:
    prom_mayor = 'Carrera 1'
elif (prom_1 == prom_2) and (prom_1 == prom_2) and (prom_2 == prom_3):
    prom_mayor = 'Los 3 son iguales'
elif (prom_2 > prom_3):
    prom_mayor = 'Carrera 2'
else:
    prom_mayor = 'Carrera 3'

#Promedio general
if total_alumnos > 0:
    prom_general = total_notas / total_alumnos
else:
    prom_general = 0

print('El promedio de notas por carrera es: ')
print(f'Carrera 1: {prom_1}')
print(f'Carrera 2: {prom_2}')
print(f'Carrera 3: {prom_3}')
print(f'El promedio general es de {prom_general}')
print(f'La carrera con el mejor promedio es la carrera numero {prom_mayor}')
print(f'La cantidad de alumnos desaprobados es de: {alumnos_desaprobados}')
print(f'El total de errores fue de: {errores}')