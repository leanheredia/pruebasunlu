'''Diseña una función que reciba una lista, vacía o no, e incorpore números hasta que el usuario ingrese el valor “salir”. Cuando termina de ingresar los datos, la función debe retornar la lista al programa principal.
'''

def recibir(lista_llenar):
    while numero.lower() != 'salir':
        numero = input('Ingresa numeros a la lista: ')
        if numero.lower() != 'salir':
             entero = int(numero)
             lista_llenar.append(entero)


def main():
        lista = []
        lista = recibir(lista)
        print(lista)
main()