'''Pedir edad.

Condiciones:

Debe estar entre 0 y 120

Si es inválida:

Volver a pedir

Cuando sea válida:

Decir si es mayor o menor de edad
'''

edad = input('Ingresa tu edad: ')

while not (edad.isdigit()):
    print('Error. Solo numeros.')
    edad = input('Ingresa tu edad: ')

edad = int(edad)

while (edad < 0 or edad > 120):
    print('Fuera de rango. 0 a 120.')
    edad = int(input('Ingresa tu edad: '))


if edad >= 18:
    print('Eres mayor de edad.')
else:
    print('Eres menor de edad.')