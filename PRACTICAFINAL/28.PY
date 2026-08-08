'''
Escribí una función que reciba una lista y retorne True si la lista es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda), y False en caso contrario.

Ejemplos:

[1,2,3,2,1] -> True
[5,8,8,5] -> True
[1,2,3] -> False
'''

def palindromo(lista):
    es_palindromo = False
    for numero in lista:
        for i in range(len(lista)-1,-1,-1):
            if n:
                es_palindromo = True
    if es_palindromo == True:
        return True




def main():
    lista = [5,8,8,4]
    print(palindromo(lista))

main()