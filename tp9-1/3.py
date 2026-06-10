'''
. Crea una función que reciba un string como parámetro, y retorne la cantidad de letras que posee. Luego, utiliza la función para escribir un programa que solicite ingresar el nombre del usuario, y luego muestre en pantalla cuántas letras tiene ese nombre. 

'''

def numeros(a, b):
    suma = a + b
    return (suma)

def main():
    n1 = int(input('Ingresa el primer numero: '))
    n2 = int(input('Ingresa el segundo numero: '))
    resultado = numeros(n1,n2)
    print(f'El resultado es: {resultado}')
main()