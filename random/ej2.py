# Programa para registrar temperaturas del mes de junio

dia = 1

mayor = -5
dia_mayor = 1

menor = 45
dia_menor = 1

suma = 0

while dia <= 30:

    print("DIA ", dia)

    # Pedir temperatura maxima validando
    maxima = float(input("Ingrese temperatura maxima: "))

    while maxima < -5 or maxima > 45:
        print("Temperatura incorrecta")
        maxima = float(input("Ingrese temperatura maxima nuevamente: "))


    # Pedir temperatura minima validando
    minima = float(input("Ingrese temperatura minima: "))

    while minima < -5 or minima > 45 or minima > maxima:
        print("Dato incorrecto")
        minima = float(input("Ingrese temperatura minima nuevamente: "))


    # Ver mayor temperatura
    if maxima > mayor:
        mayor = maxima
        dia_mayor = dia


    # Ver menor temperatura
    if minima < menor:
        menor = minima
        dia_menor = dia


    # Sacar promedio diario y acumular
    promedio_dia = (maxima + minima)/2
    suma = suma + promedio_dia


    dia = dia + 1


# Promedio total del mes
promedio_mes = suma / 30


# Mostrar resultados
print("Dia con mayor temperatura:", dia_mayor)
print("Mayor temperatura:", mayor)

print("Dia con menor temperatura:", dia_menor)
print("Menor temperatura:", menor)

print("Promedio del mes:", promedio_mes)