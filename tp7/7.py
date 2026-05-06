import os 
opcion = 0
while opcion != 4:
    print('********MI PROGRAMA*********')
    print()
    print('1. Saludar.')
    print('2. Informar temperatura.')
    print('3. Mostrar nombre de materia.')
    print('4. Salir.')
    opcion = int(input('Seleccione una opcion [1-4]: '))
    
    if opcion == 1:
        print('Hola, usuario!')
    elif opcion == 2:
        print('La temperatura actual en Chivilcoy es de: 21C')
    elif opcion == 3: 
        print('El nombre de la materia es Introduccion a la Programacion')
    else:
        print('Saliste correctamente.')
        