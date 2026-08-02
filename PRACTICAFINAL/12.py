'''Tenés una lista de palabras:

palabras = ["sol", "computadora", "gato", "programacion", "python", "mesa"]

Escribí una función:

def palabra_mas_larga(lista):

que devuelva la palabra con más letras.

En este caso debería devolver:

"programacion"
'''

def palabra_mas_larga(lista):
    palabra_mayor = lista[0]
    for palabra in lista:
        if len(palabra) > len(palabra_mayor):
            palabra_mayor = palabra
    return palabra_mayor




def main():
    lista = ['sol', 'computadora', 'gato']
    print(palabra_mas_larga(lista))

main()