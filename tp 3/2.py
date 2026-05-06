#2. Crea un script que almacene tu nombre de pila en una variable, y luego muestre en pantalla la cantidad de letras de ese nombre, con el mensaje “El nombre [NOMBRE] tiene [N] letras.”. 

mi_nombre = input('Ingresa tu nombre: ')

cantidad_letras = len(mi_nombre)

print('El nombre', mi_nombre, 'tiene', cantidad_letras, 'letras.')