'''
Realiza una función que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida:
Ejemplo: L1=['Di', 'buen', 'día', 'a', 'papa'] devolverá   ['papa', 'a', 'día', 'buen', 'Di']
'''

def invertir(lista):
    lista_invertida = []
    for i in range(len(lista)-1,-1,-1):
        lista_invertida.append(lista[i])
    return lista_invertida



def main():
    lista_original = ['Pepe', 'Hola']
    print(lista_original)
    print(f'{invertir(lista_original)}')

main()