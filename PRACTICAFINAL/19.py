'''
Escriba una función de Python que reciba una lista de números y devuelva el segundo valor más grande.
 Asegúrese de que la función maneje correctamente las listas con valores duplicados (por ejemplo, si la lista es [20, 9, 20], 
 el segundo más grande es 9).

'''
def segvalor(lista):
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
    lista = [20, 13, 9]
    print(segvalor(lista))
main()