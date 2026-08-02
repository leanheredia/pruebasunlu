''''Escribí una función que reciba una lista y devuelva el menor número.

Sin usar min().
'''


def menor(lista):
    numero_menor = lista[0]
    for numero in lista:
        if numero < numero_menor:
            numero_menor = numero
    return numero_menor








def main():
    lista = [3,5,1,4,2]
    print(menor(lista))
main()