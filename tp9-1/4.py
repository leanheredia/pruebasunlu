'''
4. Crea una función que reciba dos números como parámetro (base y exponente), y retorne el resultado de elevar base a la potencia exponente.      
'''

def funcion(base, exponente):
    calculo = base ** exponente
    return calculo
def main():
    b = int(input('Ingrese una base: '))
    e = int(input('Ingresa el exponente: '))
    resultado = funcion(b,e)
    print(f'El resultado de elevar {b} a {e} es {resultado}')
main()