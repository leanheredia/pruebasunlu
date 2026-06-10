'''
6. Modifica la función del ejercicio anterior para que retorne dos versiones del string recibido como parámetro: primero la versión en minúsculas, y luego la versión en mayúsculas. 

'''

def funcion(texto):
    mayus = texto.upper()
    minus = texto.lower()
    return mayus, minus
def main():
    letras = input('Ingresa un texto para convertir a mayusculas y minusculas: ')
    conversion = funcion(letras)
    print(conversion)
main()