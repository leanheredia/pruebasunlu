numerador = int(input('Ingresa el numerador: '))
denominador = int(input('Ingresa el denominador: '))

if (denominador == 0):
    print('No se puede dividir por 0!')
else:
    resultado = (numerador / denominador)
    print('El resultado de la division es', resultado)