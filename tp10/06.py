'''Escribe funciones que dada una cadena de caracteres:
Imprima los dos primeros caracteres.
Imprima los tres últimos caracteres.
Imprimir dicha cadena en sentido inverso.
'''

def dosprimcaract(p):
    return(p[:2])

def tresultcaract(p):
    return(p[-3:])

palabra = 'leandro'
print(dosprimcaract(palabra))
print(tresultcaract(palabra))