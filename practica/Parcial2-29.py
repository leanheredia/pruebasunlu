'''
Escribe una función que reciba una lista de números y devuelva:

la suma total
el valor máximo
el valor mínimo
'''

def obtenersumatotal(lista):
    sumatoria = 0
    for numero in lista:
        sumatoria += numero
    return sumatoria



def valor_maximo(lista):
    acumulador_mayor = -999999999999
    for numero in lista:
        if numero > acumulador_mayor:
            acumulador_mayor = numero

    return acumulador_mayor

def valor_minimo(lista):
    acumulador_menor = 99999999999999
    for numero in lista:
        if numero < acumulador_menor:
            acumulador_menor = numero
    return acumulador_menor


def main():
    lista = [-10,1,2,4,10,7,8,30]
    print(f'La suma total de los numeros es {obtenersumatotal(lista)}')
    print(f'El numero mayor es {valor_maximo(lista)}')
    print(f'El numero menor es {valor_minimo(lista)}')


main()