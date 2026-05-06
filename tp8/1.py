'''
Crea un script que le solicite al usuario ingresar una temperatura en grados Celsius, y valide que la entrada es correcta, teniendo en cuenta que la temperatura debe ser un valor numérico, y el rango válido está entre -18 y 50. El programa debe permitir ingresar el dato cuantas veces sea necesario, hasta que el usuario provea un dato válido. Procure informar al usuario cuando su dato es inválido, y cuáles son los valores aceptados. 
'''

temperatura = input('Ingresa una temperatura entre -18 y 50 grados celsius: ')

while temperatura.isalpha() or int(temperatura) <= -18 or int(temperatura) >= 50:
    if temperatura.isalpha():
        print('Debe ingresar un valor numerico')
    else: 
        print('Debe ingresar una temperatura entre -18 y 50')
    temperatura = input('Ingrese la temperatura entre -18 y 50 grados celsius: ')
print(f'La temperatura es {temperatura}.')