'''5. Crea un script que le solicite al usuario ingresar cuál es su color favorito, limitando las opciones a rojo, verde, y azul. Aclaraciones: 
- Puedes asumir que el usuario ingresará los strings en minúsculas. Opcionalmente, puedes investigar el uso de las funciones upper() y lower() para transformar la entrada a mayúsculas o minúsculas y evitar así posibles errores de validación por este detalle. 
- Al validar entre un conjunto de opciones prefijadas (en lugar de hacerlo  un rango), es posible que no sea necesario validar el tipo del dato ingresado por teclado. 
- Al detectar un dato inválido, el programa debe darle las siguientes opciones al usuario:
** DATO INVÁLIDO ** 
1. Reintentar. 
2. Salir. 
- La opción 1. Reintentar le permite al usuario ingresar el dato de manera indefinida, siempre mostrando las opciones ante cada intento fallido.
    - La opción 2. Salir finaliza el programa. 
'''

color = ''
decision = ''

while decision != '2':
    color = input('Ingresa tu color favorito: ').lower()

    if color == 'rojo' or color == 'verde' or color == 'azul':
        print(f'Tu color favorito es: {color}')
        decision = '2'
    else:
        print('**DATO INVALIDO**')
        print('1. Reintentar.')
        print('2. Salir.')
        decision = input('Ingresa una opcion: ')
        if decision == '1':
            print('')
        elif decision == '2':
            print('Saliendo')
        else: 
            print('Opcion no valida')