'''
Unión ordenada: Toma dos listas de números ya ordenadas de menor a mayor y combínalas en una tercera lista, asegurándote de que la lista final también esté ordenada de menor a mayor.

'''

def ordenar(lista, lista2):
    lista_final = []
    i = 0
    j = 0
    while i < len(lista) and j < len(lista2):
        if lista[i] < lista2[j]:
            lista_final.append(lista[i])
            i += 1












def main():
    lista_men_may = [1,2,3,4,5]
    lista2 = [6,7,8,9,10]    


main()