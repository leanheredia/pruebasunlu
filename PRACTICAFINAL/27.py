'''Escribí una función llamada invertir(lista) que reciba una lista de números y retorne una nueva lista con los elementos en orden inverso.

Ejemplo

Entrada:

[3, 8, 1, 9, 5]

Salida:

[5, 9, 1, 8, 3]
'''

def invertir(lista):
    lista_nueva = []
    for numero in range(len(lista)-1,-1,-1):
        lista_nueva.append((lista[numero]))

    return lista_nueva





def main():
    lista = [3,8,1,9,5]
    print(invertir(lista))
main()