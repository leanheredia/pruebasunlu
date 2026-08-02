'''
Una biblioteca guarda los códigos de los libros prestados durante el día.

Los códigos pueden repetirse porque un mismo libro puede prestarse varias veces.

Escribí una función que devuelva el código que más veces fue prestado.

Ejemplo:

[101, 205, 101, 330, 205, 101, 500]

Debe devolver:

101

Porque aparece 3 veces.

Otro ejemplo:

[7,9,7,9]

Puede devolver:

7 o 9


(cualquiera de los dos está bien porque ambos aparecen la misma cantidad de veces).
'''

def codigo(lista):
    mayor_conteo = 0
    codigo_mas_repetido = 0
    for codigo in lista:
        cont_numero = 0
        for otro_codigo in lista:
            if codigo == otro_codigo: 
                cont_numero += 1    
        if cont_numero > mayor_conteo:
                    mayor_conteo = cont_numero
                    codigo_mas_repetido = codigo            
    return codigo_mas_repetido

def main():
    lista = [434, 321, 101, 330, 205, 101, 500]
    print(codigo(lista))
main()