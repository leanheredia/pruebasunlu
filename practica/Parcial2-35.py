'''
Una empresa tiene dos listas con códigos de productos vendidos en dos sucursales.

L1 = [100, 200, 300, 400, 500]
L2 = [150, 200, 350, 400, 700]

Realizar una función que reciba ambas listas y retorne una nueva lista con los códigos que aparecen en las dos.

Resultado:

[200, 400]
'''


def codigo_repetido(l1, l2):
    lista_nueva = []
    for codigo in range(len(l1)):
        for codigo2 in range(len(l2)):
            if l1[codigo] == l2[codigo2]:
                lista_nueva.append(l1[codigo])
    return lista_nueva







def main():
    l1 = [100, 200, 300, 400, 500]
    l2 = [150, 200, 350, 400, 700]
    print(codigo_repetido(l1, l2))

main()