print('Ingresa las notas de los parciales: ', 'si desea detenerse ingrese -1')

contador_notas = 0
parciales = 0

while True:
    notas = float(input(f'Ingresa la nota del parcial {parciales + 1}: '))
  
    if notas == -1:
        break
    if notas < 0:
        print('Ingrese una nota valida.')
    else: 
        parciales += 1
        contador_notas += notas
        
if parciales > 0:
    promedio = contador_notas / parciales
    print(f'El promedio es: {promedio}')

print()