#6. Crea un script que le solicite al usuario ingresar 10 números, y una vez ingresados, le muestre en pantalla cuál es el máximo, y en qué posición lo ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9, y 33, se le debería mostrar el mensaje “El mayor número ingresado es 89, y lo ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1. 

posicion_max = 0
posicion_min = 0
maximo = -9999
minimo = 9999
for i in range(1, 11):
    num_usuario = int(input('Ingresa un numero entero: '))
    if num_usuario > maximo:
            maximo = num_usuario
            posicion_max = i
    elif num_usuario < minimo:
            minimo = num_usuario
            posicion_min = i
print('el valor maximo ingresado es: ', maximo, 'en la posicion', posicion_max)
print('el numero minimo es: ', minimo,  'en la posicion: ', posicion_min)