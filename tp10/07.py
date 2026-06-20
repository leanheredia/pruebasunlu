'''Escribe una función que reciba una cadena que contiene un largo número entero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe '1234567890', debe devolver '1.234.567.890'.
'''

def separar_miles(numero):
    resultado = ""
    contador = 0

    for i in range(len(numero)-1, -1, -1):
        resultado = numero[i] + resultado
        contador += 1

        if contador % 3 == 0 and i != 0:
            resultado = "." + resultado

    return resultado
def main():
	variable = input("Ingrese números: ")
	res = separar_miles(variable)
	print(res)
main()


    

