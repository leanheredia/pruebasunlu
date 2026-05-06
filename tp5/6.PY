#6. Crea un script que, dado un número de día de la semana ingresado por teclado, muestre el nombre de ese día en lenguaje natural. La relación entre números y días de la semana es la siguiente: 
''' 
1 = Domingo
2 = Lunes. 
3 = Martes. 
4 = Miércoles. 
5 = Jueves. 
6 = Viernes. 
7 = Sábado. 
'''

dia_usuario = int(input('Ingresa un dia de la semana (1 - 7): '))

if dia_usuario == 1:
    print('El nombre de ese dia es domingo')
elif dia_usuario == 2:
    print('El nombre de ese dia es Lunes')
elif dia_usuario == 3:
    print('El nombre de ese dia es Martes')
elif dia_usuario == 4:
    print('El nombre de ese dia es Miercoles')
elif dia_usuario == 5:
    print('El nombre de ese dia es Jueves')
elif dia_usuario == 6:
    print('El nombre de ese dia es Viernes')
elif dia_usuario == 7:
    print('El nombre de ese dia es Sabado')
