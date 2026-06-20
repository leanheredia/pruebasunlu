'''
Crea una función que reciba una lista y devuelva una nueva lista con los elementos en orden inverso, sin usar reverse() ni sort().
'''

def invertirlista(lista):
    lista_inversa = []

    for elemento in range(len(lista)-1,-1,-1):
        box = lista[elemento]
        lista_inversa.append(box)

    return lista_inversa


def main():
    lista = ['Pepe', 'Dia', 'Buen']
    print(lista)
    print(invertirlista(lista))
main()