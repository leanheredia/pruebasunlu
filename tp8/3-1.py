#Modifica todos los ejercicios anteriores para que en lugar de permitir reintentos de manera ilimitada, el programa permita sólo 10 reintentos. Si el usuario supera el límite de reintentos, el programa debe terminar con el mensaje “Usted está jugando conmigo, yo me retiro”.

temperatura = input('Ingresa una temperatura entre -18 y 50 grados celsius: ')
intentos = 0

while (temperatura.isalpha() or (int(temperatura) <= -18 or int(temperatura) >= 50)) and intentos <= 10:
    if temperatura.isalpha():
        print('Debe ingresar un valor numerico')
    else: 
        print('Debe ingresar una temperatura entre -18 y 50')

    
    intentos += 1
    print(f'Van {intentos} intentos.')
    temperatura = input('Ingrese la temperatura entre -18 y 50 grados celsius: ')
    
    

if temperatura.isalpha() or int(temperatura) <= -18 or int(temperatura) >= 50:
        print('Ustede esta jugando conmigo, yo me retiro.')
else:
    print(f'La temperatura es {temperatura}.')