'''Una lista contiene números enteros:

lista = [5, 8, 3, 8, 2, 5, 8, 1]

Escribí una función:

def cantidad_distintos(lista):

que devuelva cuántos números distintos hay.

Ejemplo:

[5, 8, 3, 8, 2, 5, 8, 1]

Los distintos son:

5
8
3
2
1

Por lo tanto debe devolver:

5'''

def cantidad_distintos(lista):
    distintos = []
    
    for numero in lista:
        encontrado = False
        for d in distintos:
            if numero == d:
                encontrado = True
        if encontrado == False:
            distintos.append(numero)
    return len(distintos)

def main():
    lista = [5, 8, 3, 8, 2, 5, 8, 1]
    print(cantidad_distintos(lista))
main()