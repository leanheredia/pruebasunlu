'''
Ejercicio — Segundo número mayor

Escribí una función:

def segundo_mayor(lista):

Que reciba una lista como:

[8, 15, 3, 12, 10]

Y devuelva:

12

Porque:

mayor → 15
segundo mayor → 12

'''

def segundo_mayor(lista):
    mayor = lista[0]
    segund_mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            segund_mayor = mayor
            mayor = numero
        else:
            if numero > segund_mayor:
                segund_mayor = numero
    return segund_mayor


def main():
    lista = [8, 15, 3, 12, 10]
    print(segundo_mayor(lista))

main()