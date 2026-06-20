'''
Dada una lista de números enteros y un entero k, escribe una función para cada uno de los siguientes ítems:
Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
Devuelva una lista con aquellos que son múltiplos de k.

'''
#Crear lista en main
#Crear k = numero entero x
#Funcion que devuelva tres listas:
#lista_menores = [], lista_mayores = [], lista_iguales = [] (return)
#Funcion que devuelva lista con
#lista_multiplos_k = []

def funcion(lista, k):
    lista_menores = []
    lista_mayores = []
    lista_iguales = []
    for numero in lista:
        if numero > k:
            lista_mayores.append(numero)   
        elif numero < k:
            lista_menores.append(numero)
        else:
            lista_iguales.append(numero)
    return lista_mayores, lista_menores, lista_iguales

def multiplos(lista, k):
    lista_multiplos = []
    for numero in lista:
        if numero % k == 0:
            lista_multiplos.append(numero)
    return lista_multiplos



def main():
    lista = [2,4,6,5,8,30]
    k = 5
    lista_mayores, lista_menores, lista_iguales = funcion(lista,k)
    print(f'Los numeros mayores a {k} son {lista_mayores}')
    print(f'Los numeros menores a {k} son {lista_menores}')
    print(f'Los numeros iguales a {k} son {lista_iguales}')
    print(f'Los multiplos de {k} son {multiplos(lista, k)}')
main()