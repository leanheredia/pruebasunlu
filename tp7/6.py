numero_usuario = int(input('Ingresa un numero entre 1 y 10: '))
numero_secreto = 8
intentos = 1
por_debajo = 0
por_arriba = 0
while numero_usuario != numero_secreto:
    if numero_usuario >= 1 and numero_usuario <= 10:
         intentos += 1
         print('El numero no era ese.')
         if numero_usuario < numero_secreto:
            por_debajo += 1
         elif numero_usuario > numero_secreto:
            por_arriba += 1
    else:
        print('Ingreso un valor fuera del rango.')
  
    numero_usuario = int(input('Ingresa otro numero entre 1 y 10: '))

print('Felicidades! El numero era 8.')
print(f'La cantidad de intentos fue de: {intentos}')
print(f'La cantidad de numeros por encima fue de {por_arriba}')
print(f'La cantidad de numeros por debajo fue de {por_debajo}')