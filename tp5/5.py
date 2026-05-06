#5. Crea un script que le solicite al usuario ingresar un número por teclado, y le informe con un mensaje si su número es positivo, negativo, o 0.

num_usuario = int(input('Ingresa un numero: '))

if (num_usuario > 0):
    print('El numero', num_usuario, 'es positivo')
elif (num_usuario == 0):
    print('El numero', num_usuario, 'tiene valor 0')
else:
    print('El numero', num_usuario, 'es negativo.')