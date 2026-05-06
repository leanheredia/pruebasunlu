# Crea un script que le solicite al usuario ingresar un número entero, y muestre en pantalla el factorial de dicho número. 
# NOTA: Puede obviar la validación en este ejercicio, pero recuerda que la función range no incluye al valor máximo enviado como parámetro. 
#factorial de n = n! = 1 * 2 * 3 * … * (n - 1) * n 


num_usuario = int(input('Ingresa un numero entero: '))
factorial = 1

for i in range(1, num_usuario + 1):
    factorial *= i
    print(i)
print(factorial)