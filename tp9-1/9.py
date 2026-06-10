'''
9. Crea un test unitario para el ejercicio 4. Utilice al menos 3 casos con distintos parámetros. 
'''
def funcion(base, exponente):
    calculo = base ** exponente
    return calculo

def test_funcion():
    print('Probando...')
    assert funcion(3,0) == 1
    assert funcion(5,2) == 25
    assert funcion(-3,2) == 9
    assert funcion(2,-1) == 1/2
    print('Paso okay.')

def main():
    #b = int(input('Ingrese una base: '))
    #e = int(input('Ingresa el exponente: '))
    #resultado = funcion(b,e)
    #print(f'El resultado de elevar {b} a {e} es {resultado}')
    test_funcion()
main()


