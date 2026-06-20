'''
Dada una lista de números enteros, escribe una función para cada uno de los siguientes ítems:
Devuelva una lista con todos los números  que sean primos.
Devuelva la sumatoria y el promedio de los valores.
Devuelva una lista con el factorial de cada uno de esos números.

'''

def numerosprimos(lista):
    lista_primos = []
    for numero in lista:
        bandera = True
        for i in range(2,numero):
            if numero % i == 0:
                bandera = False
            
        if bandera == True:
            lista_primos.append(numero)
    return lista_primos

def sumatoria_promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero

    promedio = suma / len(lista)

    return suma, promedio

def factorial(lista):
    lista_factorial = []
    
    for numero in lista:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        lista_factorial.append(factorial)
    return lista_factorial



def main():
    lista_original = [2,4,8,3]

    sumatoria, promedio = sumatoria_promedio(lista_original)
    print(f'Los numeros primos en la lista son: {numerosprimos(lista_original)}')
    print(f'La sumatoria de los numeros es: {sumatoria}, y el promedio es {promedio}')
    print(f'El factorial de cada numero es: {factorial(lista_original)}')

main()