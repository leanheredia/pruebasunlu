#4. Crea un script que le solicite al usuario ingresar dos números por teclado, y luego indique por pantalla cuál de ellos es el mayor. Contempla la posibilidad de que los números sean iguales, y muestre un mensaje acorde. 

num1 = int(input('Ingresa el primer numero: '))
num2 = int(input('Ingresa el segundo numero: '))

if (num1 > num2):
    print('El numero', num1, 'es mayor a', num2)
elif (num1 == num2):
    print('El numero', num1, 'es igual a', num2)
else:
    print('El numero', num1, 'es menor a', num2)