'''
Escribir una función que reciba:

lista = [8, 2, 10, 5]
numero = 10

y retorne

True

si el número está en la lista.

Si no está, retornar

False

No usar in.
'''


def verificar(lista, numero):
    bandera = False
    for n in lista:
        if n == numero:
            bandera = True

    return bandera



def main():
    lista = [8, 2, 10, 5]
    numero = 2
    print(verificar(lista,numero))

main()