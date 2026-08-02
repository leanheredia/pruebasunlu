'''
Consigna 2: La empresa "Vendemos Todo" vende accesorios para el Mundial en Argentina, Uruguay y Brasil, lleva la información de las ventas en cada país en tres listas. La empresa desea saber cuál o cuáles productos se venden en los tres países. Cada producto tiene un código único que va desde 10000 a 99999. Además, según el país lleva un prefijo "AR-", "UR-" y "BR-". Por ejemplo, los productos en la lista de Argentina aparecen como [AR-33322, AR-15624, AR-12335], en la de Uruguay [UR-15624, UR-12335, UR-45454] y en la de Brasil [BR-15624, BR-33445, BR-12335]. Nos piden escribir una función que reciba las tres listas y retorne una lista que contenga solo los productos que se venden en los tres países, respetando el código pero agregando el prefijo "L3-". Si las listas fueran las anteriores retornaría: [L3-15624, L3-12335].
'''


def quitarprefijo(listarg, listuy, listbr):
    sinprefijoarg = []
    sinprefijouy = []
    sinprefijobr = []
    for codigoarg in listarg:
        recortearg = codigoarg[3:8]
        sinprefijoarg.append(recortearg)
    for codigouy in listuy:
        recorteuy = codigouy[3:8]
        sinprefijouy.append(recorteuy)
    for codigobr in listbr:
        recortebr = codigobr[3:8]
        sinprefijobr.append(recortebr)

    return sinprefijoarg, sinprefijouy, sinprefijobr

def repetidos(sinprefijoarg, sinprefijouy, sinprefijobr):
    lista_repetidos = []
    for codigoarg in sinprefijoarg:
        en_listauy = False
        en_listabr = False
        for codigouy in sinprefijouy:
            if codigoarg == codigouy:
                en_listauy = True
        for codigobr in sinprefijobr:
            if codigoarg == codigobr:
                en_listabr = True


        if en_listauy == True and en_listabr == True:
            lista_repetidos.append('L3-'+ codigoarg)
    return lista_repetidos


def main():
    listarg = ['AR-33322', 'AR-15624', 'AR-12335']
    listuy = ['UR-15624', 'UR-12335', 'UR-45454']
    listbr = ['BR-15624', 'BR-33445', 'BR-12335']
    sinprefijoarg, sinprefijouy, sinprefijobr = quitarprefijo(listarg, listuy, listbr)
    print(repetidos(sinprefijoarg, sinprefijouy, sinprefijobr))
    
main()