'''
Una veterinaria registra las edades de los perros atendidos durante el día.

Escribí una función que reciba una lista de edades y devuelva cuántas veces aparece la edad más alta.

Ejemplo 1
[3,5,8,2,8,4]

Debe devolver:

2

Porque la edad máxima es 8 y aparece dos veces.

Ejemplo 2
[10,7,5]

Debe devolver

1
'''

def edadalta(lista):
    edad_maxima = lista[0]
    cant_maxima = 0
    for edad in lista:
        if edad > edad_maxima:
            edad_maxima = edad
    for n in lista:
        if n == edad_maxima:
            cant_maxima += 1
    return cant_maxima




def main():
    lista = [3,5,8,2,8,4,8,4]
    print(edadalta(lista))
main()