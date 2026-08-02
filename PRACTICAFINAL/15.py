'''
📝 Parcial Simulado #1 - Tienda

Una tienda guarda dos listas.

codigos = [101, 205, 101, 330, 205, 410, 330, 101]
cantidades = [2,   1,   4,   3,   2,   1,   5,   1]

Las listas están relacionadas por posición.

Por ejemplo:

Código 101 → se vendieron 2 unidades.
Código 205 → se vendió 1 unidad.
Código 101 → se vendieron 4 unidades.
...
Escribí una función
def producto_mas_vendido(codigos, cantidades):

que devuelva el código del producto que más unidades vendió en total.

Ejemplo

El código 101 vendió:
2 + 4 + 1 = 7
El código 330 vendió:
3 + 5 = 8
El código 205 vendió:
1 + 2 = 3
El código 410 vendió:
1

Entonces la función debe devolver:

330
'''

def producto_mas_vendido(codigos, cantidades):
    for a in codigos:
        acumulador = 0
        for j in range(len(codigos)):
            if a == codigos[j]:
                acumulador += cantidades[j]




def main():
    codigos = [101, 205, 101, 330, 205, 410, 330, 101]
    cantidades = [2,   1,   4,   3,   2,   1,   5,   1]
    print(producto_mas_vendido(codigos, cantidades))
main()