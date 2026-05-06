import os

decision = ''

while decision != 'n'.lower():
    os.system('cls')
    presupuesto = int(input('Ingresa el presupuesto de la pelicula: '))
    duracion = int(input('Ingresa la duracion de la pelicula: '))
    genero = input('Ingresa el genero de la pelicula (comedia, cienciaficcion): ').lower()

    if genero != 'comedia' and genero != 'cienciaficcion':
        print('Ese genero no es valido. Debe ser comedia o ciencia ficcion.')

    elif (duracion >= 90 and duracion <= 120) and (genero == 'comedia'):
            print('La pelicula se considera comedia estandar.')

    elif (duracion >= 120) and (genero == 'cienciaficcion'):
             print('La pelicula se considera epica de ciencia ficcion')
    
    elif presupuesto >= 100000000:
        print('La pelicula es una superproduccion')

    else:
        print('La pelicula es normal.')

    decision = input('Desea ingresar otra pelicula? (S/N): ').lower()

    if decision == 'n':
        print('Saliendo...')
