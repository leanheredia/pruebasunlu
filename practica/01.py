nombre = input('Ingresa tu nombre: ').lower()

while (nombre == '') or (nombre.isdigit()):
    print('Error.')
    nombre = input('Ingresa tu nombre: ').lower()

print(f'Tu nombre es: {nombre}')
