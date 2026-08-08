'''
Escribí una función llamada abreviar() que reciba una lista de nombres completos y retorne una nueva lista con los nombres abreviados.

Ejemplo

Entrada:

[
    "LIONEL MESSI",
    "KYLIAN MBAPPE",
    "ERLING HAALAND",
    "JULIAN ALVAREZ"
]

Salida:

[
    "L. MESSI",
    "K. MBAPPE",
    "E. HAALAND",
    "J. ALVAREZ"
]
'''


def abreviar(lista_nombres):
    lista_abreviados = []
    for nombre in lista_nombres:
    
        abreviar_nombre = nombre[0:1]
        for i in range(len(nombre)):
        nombre_abreviado = abreviar_nombre + '.' + ' ' + apellido
        lista_abreviados.append(nombre_abreviado)
    return lista_abreviados


def main():
    lista_nombres = ['LIONEL MESSI', 'KYLIAN MBAPPE', 'ERLING HAALAND', 'JULIAN ALVAREZ']
    print(abreviar(lista_nombres))

main()