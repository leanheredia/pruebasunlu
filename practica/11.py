'''
Un cliente ha solicitado un programa que le permita ingresar los mililitros de lluvia caídos diariamente en una semana, para que el programa le informe en pantalla el promedio de precipitación de esa semana. El cliente también desea saber cuál fue el día en que más llovió en la semana. 
A modo ilustrativo, un reporte generado por el programa debería verse, luego de haber leído las precipitaciones de los 7 días de la semana, así: 
El promedio de precipitaciones fue de XX ml diarios. 
El día de más precipitaciones fue el xxxxxx (nombre del día). 
Ten en cuenta que la numeración de los días de la semana comienza con el 1 para el día domingo. 
Codifica el programa para dar solución a lo solicitado por el cliente.
'''


#ingresar los mililitros de lluvia caidos dia x dia en 7 dias
#informar promedio de los 7 dias
#saber cual fue el dia que mas llovio
#(1 es domingo, 7 sabado)


dia_mas_llovio = 0
cant_max_lluvia = 0
suma_promedio = 0

for i in range(1,8):
    mldelluvia = int(input(f'Ingresa los mililitros de lluvia del dia {i}: '))
    if mldelluvia > cant_max_lluvia:
        cant_max_lluvia = mldelluvia
        dia_mas_llovio = i
    suma_promedio += mldelluvia

promedio = suma_promedio / 7
round(promedio, 2)

print(f'El promedio de los 7 dias es de {promedio}')
print(f'El día de más precipitaciones fue el {dia_mas_llovio} con {cant_max_lluvia}ml')




