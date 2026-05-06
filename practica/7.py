'''
EJERCICIO 5 — Encuesta básica mejorada

Para cada persona:

Pedir edad (termina con 0)
Validar edad (1 a 100)
Preguntar si estudia (si/no)

Mostrar:

Cuántos estudian
Cuántos no
Promedio de edad de los que estudian
'''

edad = input('Ingresa tu edad: ')
si_estudia = 0
no_estudia = 0
suma = 0

while edad != '0':

    while not edad.isdigit():
        print('Error. La edad debe ser un digito.')
        edad = input('Ingresa tu edad: ')

    edad = int(edad)

    while (edad < 1 or edad > 100):
        print('La edad debe ser entre 1 y 100.')
        edad = input('Ingresa tu edad: ')
        while not edad.isdigit():
            print('Error. La edad debe ser un digito.')
            edad = input('Ingresa tu edad: ')
        edad = int(edad)

    estudia = input('Estudias? (Si/No): ').lower()

    while estudia != 'si' and estudia != 'no':
        print('Solo se admite Si/No.')
        estudia = input('Estudias? (Si/No): ').lower()
        
    if estudia == 'si':
        si_estudia += 1
        suma += edad
    else:
        no_estudia += 1
    edad = input('Ingresa tu edad: ')
        
if si_estudia > 0:
    promedio = suma / si_estudia

print(f'Estudian {si_estudia} estudiantes.')
print(f'No estudian {no_estudia} estudiantes.')
print(f'El promedio de la edad de los que estudian es {promedio}')