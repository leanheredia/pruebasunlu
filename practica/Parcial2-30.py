'''
Dada una lista de números, crea una función que devuelva una nueva lista sin elementos repetidos (solo la primera aparición de cada uno).
'''

def elementosrepetidos(lista):
    lista_repetidos = []
    for numero in lista:
        existe = False

        for elemento in lista_repetidos:
            if elemento == numero:
                existe = True
        if existe == False:
            lista_repetidos.append(numero)
    return lista_repetidos
def main():
    lista = [1,2,3,5,7,10,10,3,3]
    print(elementosrepetidos(lista))

main()