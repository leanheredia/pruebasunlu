#1. Crea un script que almacene un número entero en una variable, y luego muestre en pantalla su valor absoluto, con el mensaje “El valor absoluto de N es |N|”. Finalmente, verifica que el programa funciona correctamente, ejecutándolo con el valor 10 en la variable (la salida debería ser 10), y luego con el valor -10 (la salida debería ser 10 nuevamente). 

num_entero = int(input('Ingresa un numero para calcular el valor absoluto: '))

valor_absoluto = abs(num_entero)

print('El valor absoluto de', num_entero, 'es:', valor_absoluto)
