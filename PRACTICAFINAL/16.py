'''
Escribe una función que dada una cadena de caracteres devuelve solamente las letras consonantes. 
Por ejemplo, si recibe 'algoritmos' debe devolver 'lgrtms'.

'''


def consonantes(palabra):
    vocales = 'aeiouAEIOU'

    for letra in palabra:
        es_vocal = False
        for vocal in vocales:
            if vocal == letra:
                es_vocal = True
        if letra.isalpha() and  es_vocal == False:
            print(letra)










def main():
    palabra = 'algoritmos'
    print(consonantes(palabra))
main()