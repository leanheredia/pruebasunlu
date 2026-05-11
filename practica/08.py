'''
Sistema de notas:

Pedir notas (termina con -1)

Condiciones:

Validar número
Validar rango (0–10)

Calcular:

Promedio
Cantidad de aprobados (≥6)
Cantidad de desaprobados (<6)
Porcentaje de aprobados
'''

notas = input('Ingrese las notas: ')
aprobados = 0
desaprobados = 0
porcentaje = 0
suma = 0
contador = 0
while notas != '-1':
    while not notas.isdigit() and notas != '-1':
        print('Error. Solo se permiten numeros.')
        notas = input('Ingrese las notas: ')
  
    notas = int(notas)

    while notas < 0 or notas > 10:
        print('Fuera de rango. Solo se permite de 0 a 10.')
        notas = input('Ingrese las notas: ')
        while not notas.isdigit():
            print('Error. Solo se permiten numeros.')
            notas = input('Ingrese las notas: ')
        notas = int(notas)
    
    if notas >= 6:
        contador += 1
        aprobados += 1
    elif notas < 6:
        contador += 1
        desaprobados += 1
    suma += notas
    notas = input('Ingrese las notas: ')
    
if contador > 0:
    promedios = suma / contador
else:
    promedios = 0

porcentaje = (aprobados / contador) * 100

print(f'El promedio de todas las notas es {promedios}')
print(f'La cantidad de alumnos aprobados es de {aprobados}')
print(f'La cantidad de alumnos desaprobados es de {desaprobados}')
print(f'El porcentaje de aprobados es de {porcentaje}')