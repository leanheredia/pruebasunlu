'''
7. Crea un script que le solicite a un alumno de la asignatura Introducción a la Programación que ingrese las notas de sus dos parciales. Como resultado, se le debe informar al alumno su situación, junto con la nota promedio. Las reglas para saber la situación de un alumno son las siguientes: 
● Para ser promovido (es decir, cursada aprobada y no requiere rendir final), el alumno debe haber aprobado ambos parciales y tener un promedio mayor o igual 	
● Para estar regular (cursada aprobada, pero debe rendir final), el alumno debe haber aprobado ambos parciales (nota mayor o igual a 4). 
● Si el alumno no ha aprobado ambos parciales (es decir, tiene nota menor que 4 en alguno de ellos), entonces queda en condición de libre (es decir, puede rendir un final extendido o recursar). 
'''

nota_parcial1 = float(input('Ingresa la nota del primer parcial: '))
nota_parcial2 = float(input('Ingresa la nota del segundo parcial: '))
promedio = (nota_parcial1 + nota_parcial2) / 2
print('Tu promedio es', promedio)


if (nota_parcial1 >= 4 and nota_parcial2 >= 4) and (promedio >= 7):
    print('Alumno promovido.  No requiere rendir final')
elif (nota_parcial1 >= 4 and nota_parcial2 >= 4) and (promedio < 7):
    print('Alumno regular. Requiere rendir examen final')
else:
    print('Alumno desaprobado. ')
    