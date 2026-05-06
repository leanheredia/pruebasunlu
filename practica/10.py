'''
1. Sistema de notas completo

No solo promedio.

Que tenga:

Carga de notas (con -1)
Validación completa
Promedio
Aprobados / desaprobados
Nota más alta y más baja (sin usar max/min, hacelo vos)
'''
contador_notas = 1
notas = input(f'Ingresa la nota numero {contador_notas}: ')
aprobados = 0
desaprobados = 0
alumnos = 0
nota_maxima = 0
nota_minima = 0
suma = 0

while notas != '-1':
    while not notas.isdigit() and notas != '-1':
        print('Error. Solo se permiten digitos.')
        notas = input(f'Ingresa la nota numero {contador_notas}: ')
    if notas != '-1':
        notas = int(notas)
        while notas < 0 or notas > 10:
            print('Solo se permite de 0 a 10.')
            notas = input(f'Ingresa la nota numero {contador_notas}: ')
    
            while not notas.isdigit():
                print('Error. Solo se permiten digitos.')
                notas = input(f'Ingresa la nota numero {contador_notas}: ')
            notas = int(notas)


        contador_notas += 1    
        if notas >= 7:
            alumnos += 1
            aprobados += 1
        else:
            alumnos += 1
            desaprobados += 1
        if alumnos == 1:
            nota_maxima = notas
            nota_minima = notas
        else:
            if notas > nota_maxima:
                nota_maxima = notas
            if notas < nota_minima:
                nota_minima = notas
        suma += notas
        notas = input(f'Ingresa la nota numero {contador_notas}: ')

if alumnos > 0:
    promedio = suma / alumnos
else:
    promedio = 0

print(f'La cantidad de alumnos ingresados fueron de {alumnos}')
print(f'La nota maxima fue de {nota_maxima}')
print(f'La nota minima fue de {nota_minima}')
print(f'El promedio es de {promedio}')