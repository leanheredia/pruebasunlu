'''

Usa las funciones para strings que ya conoces e implementa un script que haga lo siguiente:
Le solicite al usuario ingresar una palabra por teclado. Se debe validar que la palabra tenga al menos una ‘ñ’. En caso de no ser válida, se le debe pedir al usuario que la reingrese.
Informe en pantalla la cantidad de letras de la palabra ingresada.
Transforme la palabra a mayúsculas, reemplace todas las ‘Ñ’ por ‘N’, y luego muestre el resultado en pantalla.

'''



def cantidad_letras(pala):
    canti = len(pala)
    return canti
def transformar(p):
	palabra=p.upper()
	nueva=''
	for letra in palabra:
		if letra == "Ñ":
			nueva = nueva + "N"
		else:
			nueva = nueva + letra
		
		
	return nueva



def main():
    palabra = input('Ingresa una palabra: ')
    while 'ñ' not in palabra:
        print('Palabra invalida.')
        palabra = input('Ingresa una palabra: ')
    print(f'La cantidad de letras es de: {cantidad_letras(palabra)}')
    print(f'Palabra sin ñ: {transformar(palabra)}')
main()

