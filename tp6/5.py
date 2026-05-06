#5. Crea un script que le solicite al usuario ingresar 10 números enteros, y por cada uno, informarle si el mismo es positivo, negativo, o cero. 

for i in range(1,11):
    num_usuario = int(input('Ingresa un numero entero: '))
    if num_usuario > 0:
        print('El numero es positivo')
    elif num_usuario == 0:
        print('El numero es 0')
    else:
        print('El numero es negativo')