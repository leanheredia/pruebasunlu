#Una variable es un nombre que se le asigna a un espacio de memoria, funcionando así como una caja.

numero_alumnos = int(input('Ingresa la cantidad de alumnos: '))


while numero_alumnos >= 1 and numero_alumnos <= 100:
    print('El numero de alumnos debe ser mayor a 1 y menor a 100.')
    numero_alumnos = int(input('Ingresa la cantidad de alumnos: '))

if numero_alumnos >= 50:
    costo_alumno = 150.000
    pago = numero_alumnos * costo_alumno
    print('El costo por cada alumno es de 150.000$')
    print('El pago a la compañia es de', pago)

elif numero_alumnos >= 30 and numero_alumnos <= 49:
    costo_alumno = 200.000
    pago = numero_alumnos * costo_alumno
    print('El costo por cada alumno es de 200.000$')
    print('El pago a la compañia es de', pago)
else:
     por_alumno = 7000000 / numero_alumnos
     print('Costo total es de $7.000.000')
     print('El costo de colectivo es de', por_alumno)
