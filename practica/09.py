'''EJERCICIO 6 — Menú repetitivo

Mostrar un menú:

Ingresar número
Mostrar suma
Salir

Condiciones:

Validar opción (1-3)
Si elige 1 → pedir número válido y sumarlo
Si elige 2 → mostrar suma acumulada
Si elige 3 → terminar'''

print('Menu')
print('1-Ingresar numero')
print('2-Mostrar suma')
print('3-Salir')
decision = input('Ingresa una opcion (1-3): ')
suma = 0

while decision != '3':
    while not decision.isdigit():
        print('Error. Deben ser numeros.')
        decision = input('Ingresa una opcion (1-3): ')

    while decision != '1' and decision != '2' and decision != '3':
        print('Las opciones son del 1 al 3.')
        decision = input('Ingresa una opcion (1-3): ')
        while not decision.isdigit():
            print('Error. Deben ser numeros.')
            decision = input('Ingresa una opcion (1-3): ')
    
    if decision == '1':
        numero = input('Ingresa un numero entero: ')
        while not numero.isdigit():
            print('Error. Deben ser numeros enteros.')
            numero = input('Ingresa un numero entero: ')
        numero = int(numero)
        suma += numero
        decision = input('Ingresa una opcion (1-3): ')

    elif decision == '2':
        print(f'La suma de los numeros es {suma}')
        decision = input('Ingresa una opcion (1-3): ')
    else:
        print('Saliendo...')