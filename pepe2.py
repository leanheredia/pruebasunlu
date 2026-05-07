'''
Descripción:

Vas a programar la pantalla de retiro de efectivo de un cajero automático. El programa debe pedirle al usuario que ingrese el monto exacto que desea retirar, pero debe ser a prueba de fallos.

Requisitos y Validaciones:


Bucle de validación: El programa debe usar un ciclo (while) para preguntarle el monto al usuario continuamente hasta que ingrese un dato 100% válido.

Solo números: Si el usuario ingresa letras, símbolos o deja el espacio en blanco, el programa no debe fallar. Debe atrapar el error y mostrar un mensaje como "Error: Por favor, ingrese solo números" y volver a preguntar.

Monto positivo: El número ingresado debe ser mayor a 0. 

No se pueden retirar montos negativos ni 0.

Billetes disponibles: El cajero solo tiene billetes de $500. 

Por lo tanto, el monto solicitado debe ser obligatoriamente un múltiplo de 500 (ej: 500, 1000, 1500, etc.).

Éxito: Si el usuario pasa todas estas validaciones, el ciclo se rompe y el programa imprime: "Transacción exitosa. Entregando $ [monto]..."
'''

print('Cajero automatico')
monto_retirar = input('Ingresa el monto a retirar (Solo acepta billetes de $500): ')

while not (monto_retirar.isdigit()) or int(monto_retirar) <= 0:
    if not (monto_retirar.isdigit()):
        print('Error. Solo se admiten numeros')
    else:
        print('El monto a retirar debe ser mayor a 0.')
    monto_retirar = input('Ingresa el monto a retirar (Solo acepta billetes de $500): ')
monto_retirar = int(monto_retirar)

while monto_retirar % 500 != 0:
    print('El monto a retirar solo admite billetes de $500')
    monto_retirar = input('Ingresa el monto a retirar (Solo acepta billetes de $500): ')
monto_retirar = int(monto_retirar)

if monto_retirar % 500 == 0:
    print(f'Transaccion exitosa. Entregando ${monto_retirar}')