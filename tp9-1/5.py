'''
5. Crea una función que reciba un string como parámetro, y retorna el mismo string, pero con todas las letras convertidas a mayúsculas.

'''

def funcion(texto):
    mayus = texto.upper()
    return mayus
def main():
    letras = input('Ingresa un texto para convertir a mayusculas: ')
    conversion = funcion(letras)
    print(conversion)
main()