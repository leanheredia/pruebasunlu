'''

Escribí una función que reciba:

lista = [4,8,4,7,4,9]
numero = 4

Y retorne:

3 (porque aparece 3 veces)

No uses count().'''

def retornar(lista,numero):
    contador = 0
    for n in lista:
        if n == numero:
            contador += 1
    return contador






def main():
    lista = [4,8,4,7,4,9]
    numero = 4
    print(retornar(lista,numero))
main()