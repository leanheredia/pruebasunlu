numero = input('Ingresa un numero natural: ')
intentos = 1

while (not numero.isdecimal()) and intentos < 5:
    print('Su numero esta mal ingresado')
    numero = input('Ingresa un numero natural: ')
    intentos += 1

if intentos == 5:
    numero = -1


print(f'El numero ingresado es: {numero}')