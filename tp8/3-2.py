#Modifica todos los ejercicios anteriores para que en lugar de permitir reintentos de manera ilimitada, el programa permita sólo 10 reintentos. Si el usuario supera el límite de reintentos, el programa debe terminar con el mensaje “Usted está jugando conmigo, yo me retiro”.

edad = input('Ingresa tu edad: ')
intentos = 0
while (edad.isalpha() or (int(edad) < 18 or int(edad) > 60)) and intentos <= 10:
    if edad.isalpha():
        print('Debe ingresar un valor numerico.')
    else:
        print('Debe ingresar valores entre 18 y 60.')
    intentos += 1
    print(f'Van {intentos} intentos')
    edad = input('Ingresa tu edad: ')



if edad.isalpha() or int(edad) < 18 or int(edad) > 60:
        print('Ustede esta jugando conmigo, yo me retiro.')
else:
    print(f'La edad es {edad}')