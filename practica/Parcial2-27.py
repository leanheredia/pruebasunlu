'''
Crea una función que reciba una lista vacía o no, y vaya pidiendo nombres hasta que el usuario escriba "fin". Devuelve la lista completa de tripulantes.
'''

def agregar_nombres(lista):
    entrada = input('Ingresa un nombre a la lista: ')
    while entrada != 'salir'.upper():
        lista.append(entrada)
        entrada = input('Ingresa un nombre a la lista: ')
    return lista




def main():
    lista = []
    print(f'La lista con nombres es {agregar_nombres(lista)}')

main()