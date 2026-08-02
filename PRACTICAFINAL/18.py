'''
Realizar una función que reciba una Lista y dos elementos y busque el primer elemento 
especificado, en la lista, e inserte el segundo elemento como nuevo inmediatamente después.
Ejemplo si el 1er elemento es 10, el segundo 20 y la lista [7, 32, 44, 10, 15, 66] la lista debe quedar: [7, 32, 44, 10, 20, 15, 66]

'''



def encontrar(lista, e1, e2):
    lista_nueva = []
    insertado = False
    for numero in lista:
        lista_nueva.append(numero)

        if numero == e1 and not insertado:
            lista_nueva.append(e2)
            insertado = True



    return lista_nueva





def main():
    lista = [7, 32, 44, 10, 15, 66]
    e1 = 10
    e2 = 20
    print(encontrar(lista, e1, e2))
main()