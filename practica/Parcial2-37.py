'''
Ejercicio 3 - Países en común

Tres listas contienen países que clasificaron a distintos torneos.

A = ["ARG","BRA","URU","ESP"]
B = ["BRA","URU","FRA"]
C = ["URU","BRA","ITA"]

Generar una lista con los países que aparecen en las tres listas.

Resultado:

["BRA","URU"]
'''

def similitud_paises(a,b,c):
    lista_nueva = []
    for paises1 in a:
       for paises2 in b:
           if paises2 == paises1:
               for paises3 in c:
                   if paises1 == paises3:
                       lista_nueva.append(paises1)
    return lista_nueva







def main():
    a = ['ARG', 'BRA', 'URU', 'ESP']
    b = ['BRA', 'URU', 'FRA']
    c = ['URU', 'BRA', 'ITA']
    print(similitud_paises(a,b,c))

main()