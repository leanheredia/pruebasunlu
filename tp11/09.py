'''
Encuentra la cadena más larga en una lista de string.

'''

def encontrar(lista):
    cadena_mayor = lista[0]

    for palabra in lista:
        if len(palabra) > len(cadena_mayor):
            cadena_mayor = palabra
    return cadena_mayor



def main():
    lista = ['Pepe', 'Leandro', 'a', 'Acidodesixoribunucleico']
    print(encontrar(lista))
main()