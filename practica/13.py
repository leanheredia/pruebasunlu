'''
Imagina que estás intentando descifrar la clave de un candado digital antiguo. 
Este candado tiene 3 ranuras y cada ranura puede contener un dígito del 0 al 9.

Se sabe que la combinación ganadora cumple con las siguientes condiciones:

La suma de los tres dígitos debe ser exactamente igual a 15.

El primer dígito debe ser un número par.

El tercer dígito debe ser mayor que el segundo.

Tu misión:
Escribe un programa en Python que encuentre y muestre por pantalla todas las combinaciones posibles que cumplan con estas tres reglas.
'''

#combinacion de 3 digitos.
#la suma de los 3 debe ser 15.
#1 digito > par (numero % 2 == 0)
#3 digito > 2 digito

for digito1 in range(0, 10):
    for digito2 in range(0,10):
        for digito3 in range(0,10):
            if (digito1 + digito2 + digito3 == 15) and (digito1 % 2 == 0) and (digito3 > digito2):
                print(digito1, digito2, digito3)
