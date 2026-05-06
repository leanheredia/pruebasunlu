numero = input('Ingresa un numero entre el 1 al 100: ')

while not numero.isnumeric() or (int(numero) < 1 or int(numero) > 100): 
    if not numero.isnumeric():
        print('Debes ingresar un numero')
    else:
        print('Debes ingresar un valor entre 1 y 100')
    numero = input('Ingrese un numero entre el 1 al 100: ')

print(f'El numero {numero} es valido')