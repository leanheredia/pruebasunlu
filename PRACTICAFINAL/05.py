'''
Escribí una función que reciba una lista de números y devuelva el número más grande.

Ejemplo:

[8,2,15,6,11]

Debe devolver:

15
Restricciones
❌ No usar max().
❌ No ordenar la lista.
❌ No usar sort().
'''

def masgrande(lista):
    numero_guardado = lista[0]
    for numero in lista:
        if numero > numero_guardado:
            numero_guardado = numero
    return numero_guardado







def main():
    lista = [8,2,15,6,11]
    print(masgrande(lista))
main()