#8. Se le ha solicitado a dos programadores que resuelvan el mismo problema: conociendo el total de inscriptos de una asignatura y cuántos alumnos han asistido a la clase de hoy, queremos un programa que nos muestre en pantalla el porcentaje de asistencia del día de hoy. Las dos versiones que realizaron los programadores son: 
#Programador A 
# almaceno cuántos alumnos asistieron a la clase de hoy 
alumnos_presentes = 35 
# almaceno el total de inscriptos en la asignatura 
alumnos_inscriptos = 54 
# calculo del porcentaje de alumnos presentes en la clase de hoy 
porcentaje_presentes = (alumnos_presentes * 100) / alumnos_inscriptos 
# muestro el porcentaje calculado en pantalla 
print('Hoy asistió el ' + str(porcentaje_presentes) + ' porciento del alumnado.') 

#Programador B 
p = 35 
i = 54 
pp = (p * 100) / i 
print('Hoy asistió el ' + str(pp) + ' % del alumnado.') 

#- ¿Ambas versiones resuelven el problema?. 
# Si, ambas  versiones resuelven el problema correctamente.

# ¿Cuál versión es más legible y fácil de comprender?. 
# En terminos de comprensión, el programador A lo hace mas facil de entender para alguien que tiene que entender el código. 
# 
# 
# - ¿Qué desventajas tiene escribir código en la forma en que lo hace Programador B?
# El programador B puede generar confusion con el nombre de las variables, sin tener una guia.

