nombre = input('Ingresa tu nombre: ')

if nombre.isalpha():
    edad = input('Ingresa tu edad: ')
    if edad.isdigit():
        edad = int(edad)
        if edad >= 18:
            contraseña = input('Ingresa una contraseña con al menos 2 letras y 1 numero: ')
            if contraseña.isalnum():
                print('Usuario creado con exito')
            else:
                print('La contraseña no puede tener caracteres especiales como %&#,etc')
        else:
            print('Eres menor de edad, no puedes registrarte.')
else:
    print('El nombre solo puede contener letras.')
