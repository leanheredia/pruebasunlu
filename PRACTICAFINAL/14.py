'''
Ejercicio 4 — Elementos que aparecen una sola vez

Dada:

lista = [5, 8, 3, 8, 2, 5, 1]

Crear una función:

def unicos(lista):

que devuelva:

[3, 2, 1]

Porque esos números aparecen exactamente una vez.
'''

def unicos(lista):
    lista_nueva = []    
    for numero in lista:
        contador = 0
        primer_num = numero
        for num2 in lista:
            if primer_num == num2:
                contador  += 1

        if contador == 1:
            lista_nueva.append(primer_num)
    return lista_nueva



def main():
    lista = [5, 8, 3, 8, 2, 5, 1]
    print(unicos(lista))

main()