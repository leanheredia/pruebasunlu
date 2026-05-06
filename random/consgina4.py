edad1 = input('Ingresa la primera edad: ')
edad2 = input('Ingresa la segunda edad: ')
edad3 = input('Ingresa la tercera edad: ')

while (edad1 < 1 or edad1 > 100) or (edad2 < 1 or edad2 > 100) or (edad3 < 1 or edad3 > 100):
    print('La edad tiene que ser entre 1 y 100.')
    edad1 = input('Ingresa la primera edad: ')
    edad2 = input('Ingresa la segunda edad: ')
    edad3 = input('Ingresa la tercera edad: ')

if (edad1 > edad2) and (edad1 > edad3):
    print('La edad 1 es la mayor.')
elif (edad2 > edad3):
    print('La edad 2 es la mayor.')
elif (edad1 == edad2 and edad1 == edad3) and (edad2 == edad3):
    print('Las 3 son iguales')
else:
    print('La edad 3 es la mayor.')