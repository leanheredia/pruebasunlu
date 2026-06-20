def comparar_listas(lista_nueva, listaar, listabr, listauy):
    lista_nueva.append('l3-codigo')
    for productoar in range(len(listaar)):
            elemento = listaar[productoar]
            lista_nueva.append(elemento)

    for productobr in range(len(listabr)):
        elemento = listabr[productobr]
        encontrado = False
        for g in range(len(lista_nueva)):
              if elemento == lista_nueva[g]:
                   encontrado == True
        if encontrado == True:
            lista_nueva.append(elemento)

    for productouy in range(len(listauy)):
        elemento = listauy[productouy]
        encontrado2 = False
        for x in range(len(lista_nueva)):
            if elemento == lista_nueva[x]:
                encontrado2 == True
        if encontrado2 == True:
             lista_nueva.append(elemento)

    return lista_nueva



def main():
    lista_nueva = []
    listaar = [26636, 'Remera', 'Buzo', 'Insumos']
    listabr = [62627,  'Pantalon', 'Remera', 'Insumos']
    listauy = [62627, 'Insumos', 'Buzo', ]
    print(comparar_listas(lista_nueva, listaar, listabr, listauy))
main()