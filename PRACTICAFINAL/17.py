'''
Escribe una función que reciba una cadena de unos y ceros 
(es decir, un número en representación binaria) y devuelva el valor decimal correspondiente.

'''

def binario(binario_string):
    decimal = 0
    for n in range(len(binario_string)):
        if binario_string[n] == '1':
            posicion_derecha = len(binario_string) -1 - n
            decimal += 2**posicion_derecha
    return decimal







def main():
    binario_string = '1000011'
    print(binario(binario_string))
main()