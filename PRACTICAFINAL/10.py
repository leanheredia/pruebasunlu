'''
Una tienda tiene una lista con las ventas de sus productos:

ventas = [5, 2, 8, 8, 3, 8, 1]

Cada posición representa un producto:

Producto:  0  1  2  3  4  5  6
Ventas:    5  2  8  8  3  8  1

Hacé una función:

def producto_mas_vendido(ventas):

que devuelva la posición del producto que más vendió.

En este caso debería devolver:

2

porque el producto 2, 3 y 5 tienen 8 ventas, pero nos quedamos con el primero que apareció.
'''


def masvendido(lista):
    mas_vendio = lista[0]
    posicion_mas_vendio = 0
    for i in range(len(lista)):
        if lista[i] > mas_vendio:
            mas_vendio = lista[i]
            posicion_mas_vendio = i
    return posicion_mas_vendio



def main():
    lista = [5,2,8,8,3,8,1]
    print(masvendido(lista))

main()