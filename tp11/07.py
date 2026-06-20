'''
Escribe una función que reciba una cadena a buscar y una lista de nombres de personas y  busque dentro de la lista, todas los elementos que contengan esa cadena o cualquier parte de ella. Debe devolver una lista con los elementos encontrados.

'''
#Funcion busque nombre dentro de una lista de personas

def buscar(objetivo, lista):
    lista_nueva = []
    largo_objetivo = len(objetivo)
    for nombre in lista:
        largo_nombre = len(nombre)
        bandera = False

        for i in range(largo_nombre - largo_objetivo + 1):
            pedacito = nombre[i : i + largo_objetivo]
            if pedacito == objetivo:
                bandera = True
                
        if bandera == True:
            lista_nueva.append(nombre)
    return lista_nueva

def main():
    lista = ['Pedro', 'Lautaro','Jose', 'Alberto', 'Lautaro']
    objetivo = 'Lautaro'
    print(buscar(objetivo, lista))
main()