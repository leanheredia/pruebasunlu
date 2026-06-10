'''
7. Crea una función que reciba dos string como parámetro (nombre1 y nombre2), y retorne True si nombre1 tiene más letras que nombre2, o False en caso contrario. nom1=input("Ingrese Nombre 1 ")

'''

def funcion(nom1, nom2):
    if len(nom1) > len(nom2):
        return True
    else:
        return False

def main():
    texto1 = input('Ingrese el primer texto: ')
    texto2 = input('Ingrese el segundo texto: ')
    res = funcion(texto1, texto2)
    print(res)
main()