nota = input('Ingresa una nota: ')

while not (nota.isdigit()) or (int(nota) < 0 or int(nota) > 10):
    if not (nota.isdigit()):
        print('Error. Solo se admiten numeros')
    else:
        print('Error. Rango invalido.')
    nota = input('Ingresa una nota: ')
nota = int(nota)

if nota >= 0 and nota <= 3:
    print('Desaprobado')
elif nota >= 4 and nota <= 6:
    print('Regular')
elif nota >= 7 and nota <= 9:
    print('Bueno')
elif nota == 10:
    print('Excelente')