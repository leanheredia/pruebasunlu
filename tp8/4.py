'''
4. La técnica de validación para un conjunto específico de valores se puede utilizar para construir menús de opciones. Construye un menú que le muestre al usuario lo siguiente: 
********* MI PROGRAMA ********* 
1. Saludar. 
2. Informar temperatura. 
3. Mostrar nombre de materia. 
4. Salir. 
Seleccionar una opción [1-4]: 
- Cuando el usuario ingrese la opción 1, se mostrará el mensaje “Hola, bienvenido a mi programa interactivo!”. 
- Cuando el usuario ingrese la opción 2, se mostrará el mensaje “Hay una sensación térmica de 20 grados Celsius.”. 
- Cuando el usuario ingrese la opción 3, se mostrará el mensaje “Estás en la materia Introducción a la Programación!”. 
- Cuando el usuario ingrese la opción 4, el programa debe terminar, mostrando el mensaje “Hasta la próxima!”. 
- Si el usuario ingresa una opción inválida, se muestra el mensaje “Opción inválida.”. 
'''

decision = ''


while decision != '4':
    print('********* MI PROGRAMA *********')
    print('1. Saludar.')
    print('2. Informar temperatura.')
    print('3. Mostrar nombre de materia.') 
    print('4. Salir.')
    decision = input('Seleccionar una opción [1-4]: ')

    if not decision.isdigit() or (decision.isdigit() and (int(decision) < 1 or int(decision) > 4)):
        print('Elige una opcion correcta, solo letras.')
    elif decision.isdigit():
        decisionint = int(decision)
    
        if decisionint == 1:
            print('Hola, bienvenido a mi programa interactivo!')
        elif decisionint == 2:
            print('Hay una sensación térmica de 20 grados Celsius.')
        elif decisionint == 3:
            print('Estás en la materia Introducción a la Programación!')
        elif decisionint == 4:
            print('Hasta la próxima!')
            