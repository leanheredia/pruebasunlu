'''
Escribe una función que reciba:

una cadena
una lista de palabras o nombres
y devuelva una lista con todos los elementos que contengan esa cadena en cualquier parte.

'''


def obtener_cadena(cadena, lista):
    lista_nueva = []
    for elemento in lista:
            bandera = False
            for i in range(len(elemento)):
                fragmento = elemento[i:i+len(cadena)]
                if fragmento == cadena:
                     bandera = True

            if bandera == True:
                lista_nueva.append(elemento)
    return lista_nueva
def main():
    cadena = 'Me'
    lista = ['Mesa', 'Silla', 'Lorenzo', 'Agustin', 'Enzo']
    print(f'El string {cadena} aparece en la/s palabra/s {obtener_cadena(cadena, lista)}')
main()