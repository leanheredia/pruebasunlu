'''
Ejercicio 1

Una empresa guarda los códigos de sus empleados de la siguiente manera:

A4821
C1938
B7777
A9384

Cada código posee:

una letra inicial (A, B o C)
cuatro números.

Escribir una función que reciba una lista con esos códigos y genere otra lista donde:

si el número es par, la letra se mueve al final
si el número es impar, la letra permanece al principio
En ambos casos los cuatro números aparecen invertidos.

Ejemplo

A4821

↓

A1284
B2468

↓

8642B

No se permite usar slicing ([::-1]).
'''

def recibirlista(lista_codigos):
    lista_final = []
    for codigo in lista_codigos:
        letra = codigo[0]
        numeros_str = codigo[1:]
        entero = int(numeros_str)

        numeros_invertidos = ''
        for i in range(len(numeros_str)-1,-1,-1):
            numeros_invertidos += numeros_str[i]

        if entero % 2 == 0:
            res = numeros_invertidos + letra
        else:
            res = letra + numeros_invertidos

        lista_final.append(res)
    return lista_final            

def main():
    lista_codigos = ['A15', 'B12']
    print(recibirlista(lista_codigos))

main()