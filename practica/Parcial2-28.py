'''
Dada una lista de números enteros:

Devuelve una lista con los pares
Devuelve otra con los impares
Devuelve otra con los múltiplos de 3
'''

def obtener_pares(lista):
    lista_pares = []
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return lista_pares

def obtener_impares(lista):
    lista_impares = []
    for numero in lista:
        if numero % 2 != 0:
            lista_impares.append(numero)
    return lista_impares

def multiplos_tres(lista):
    lista_multiplos_3 = []
    for numero in lista:
        if numero % 3 == 0:
            lista_multiplos_3.append(numero)
    return lista_multiplos_3

def main():
    lista = [1,2,4,5,6,9,15]
    print(f'La lista con los numeros pares solamente es: {obtener_pares(lista)}')
    print(f'La lista con los numeros impares solamente es: {obtener_impares(lista)}')
    print(f'La lista con los numeros multiplos de 3 solamente es: {multiplos_tres(lista)}')

main()