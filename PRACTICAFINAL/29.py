'''
Escribe funciones que dada una cadena de caracteres:
Imprima los dos primeros caracteres.
Imprima los tres últimos caracteres.
Imprimir dicha cadena en sentido inverso.

'''

def dosprimeros(string):
    dosprimeroschar = string[0:2]

    return dosprimeroschar

def tresultimos(string):
    tresultimoschar = string[-3:]
    return tresultimoschar

def senti(string):
    for i in range(len(string)-1,-1,-1):
        dadovuelta = string[i]
    return dadovuelta







def main():
    string = 'Messi'
    ds = dosprimeros(string)
    tu = tresultimos(string)
    sen = senti(string)
    print(ds)
    print(tu)
    print(sen)


main()