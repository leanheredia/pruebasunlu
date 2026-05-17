'''
La consultora "Ya te Consulto", realizó una encuesta para saber el uso de "IA" según los rangos de edades, para ello se elaboró un formulario donde se pregunta: Edad y Días x semana que usa IA. Se obtuvieron 3815 respuestas, nos piden un programa en Python que cargue y procese la información del formulario e informe cuál es el rango de edad que en promedio más usa la "IA" y cuál el que menos la usa. Los rangos de edad son: 16 a 26, 27 a 47 y 48 o más.
'''
dias_16_26 = 0
dias_27_47 = 0
dias_mas_48 = 0
personas_16_26 = 0
personas_27_47 = 0
personas_mas_48 = 0


for i in range(3850):
    edad = int(input('Ingresa tu edad: '))
    dias_ia = int(input('Ingresa la cantidad de dias por semana que usas IA: '))
    if edad >= 16 and edad <= 26:
        personas_16_26 += 1
        dias_16_26 += dias_ia
    elif edad >= 27 and edad <= 47:
        personas_27_47 += 1
        dias_27_47 += dias_ia
    elif edad >= 48:
        dias_mas_48 += dias_ia
        personas_mas_48 += 1

#promedio
if personas_16_26 > 0:
    prom_16_26 = dias_16_26 / personas_16_26
else:
    prom_16_26 = 0
if personas_27_47 > 0:
    prom_27_47 = dias_27_47 / personas_27_47
else:
    prom_27_47 = 0
if personas_mas_48 > 0:
    prom_mas_48 = dias_mas_48 / personas_mas_48
else:
    prom_mas_48 = 0

#promedio mayor


if prom_16_26 > prom_27_47 and prom_16_26 > prom_mas_48:
    rango_mayor = 'de 16 a 26'
elif prom_16_26 == prom_27_47 and prom_16_26 == prom_mas_48:
    rango_mayor = 'son iguales'
elif prom_27_47 > prom_mas_48:
    rango_mayor = 'de 27 a 47'
else:
    rango_mayor = 'mas de 48'

if prom_16_26 < prom_27_47 and prom_16_26 < prom_mas_48:
    rango_menor = 'de 16 a 26'
elif prom_16_26 == prom_27_47 and prom_16_26 == prom_mas_48 and prom_27_47 == prom_mas_48:
    rango_menor = 'son iguales'
elif prom_27_47 < prom_mas_48:
    rango_menor = 'de 27 a 47'
else:
    rango_menor = 'mas de 48'

#prints
print(f'El rango de edad que en promedio mas usa la IA es: {rango_mayor}')
print(f'El rango de edad que en promedio menos usa la IA es: {rango_menor}')