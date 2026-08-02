'''Escribí una función que reciba una lista y devuelva otra lista sin elementos repetidos.

Ejemplo:

[4,8,4,2,8,7,4]

Debe devolver:

[4,8,2,7]
Restricciones
❌ No usar set().
❌ No usar in.
❌ No usar count().
❌ No usar break().'''



def sinrepetidos(lista):
    lista_nueva = []
    for numero in lista:
        serepite = False
        for n in lista_nueva:
            if numero == n:
                serepite = True
        if serepite == False:
            lista_nueva.append(numero)
        

    return lista_nueva


def main():
    lista = [4,8,4,2,8,7,4]
    print(sinrepetidos(lista))

main()