dado1 = int(input('Resultado del dado 1: '))
dado2 = int(input('Resultado del dado 2: '))
dado3 = int(input('Resultado del dado 3: '))

while (dado1 <1 or dado1 >6) or (dado2 <1 or dado2 >6) or (dado3 <1 or dado3 >6):
    print('El dado solo puede obtener resultados del 1 al 6.')
    dado1 = int(input('Resultado del dado 1: '))
    dado2 = int(input('Resultado del dado 2: '))
    dado3 = int(input('Resultado del dado 3: '))

if dado1 == 6 and dado2 == 6 and dado3 == 6:
    print('Excelente')
elif (dado1 == 6 and dado2 == 6) or (dado1 == 6 and dado3 == 6) or (dado2 == 6 and dado3 == 6):
    print('Muy bien')
elif (dado1 == 6) or (dado2 == 6) or (dado3 == 6):
    print('Regular')
else:
    print('Pesimo')