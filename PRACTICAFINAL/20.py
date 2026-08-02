'''
Dadas tres listas separadas, escriba una función que retorne una lista que contenga solo los elementos que aparecen en las tres.

'''

def tresel(lista1, lista2, lista3):
    lista_nueva = []
    for numero1 in lista1:
        en_lista2 = False
        en_lista3 = False
        for numero2 in lista2:
            if numero1 == numero2:
                en_lista2 = True
        for numero3 in lista3:
            if numero1 == numero3:
                en_lista3 = True
        if en_lista2 == True and en_lista3 == True:
            lista_nueva.append(numero1)
    return lista_nueva


def main():
    lista1 = [2,4,1]
    lista2 = [3,5,1]
    lista3 = [3,2,1]
    print(tresel(lista1,lista2,lista3))
main()


