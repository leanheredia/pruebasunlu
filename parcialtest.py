'''
Un contador es una variable especifica para aumentar o disminuir una cantidad fija o constante de numeros. 
Un acumulador aumenta, disminuye, multiplica o divide una cantidad variable de numeros.   
Por ej, contador es para Contar cuántas personas entran a una tienda, y acumulador para ver cuanto dinero gastaron

La precaucion es que se debe inicializarlo antes con un valor para poder usarlo
'''


'''
Consigna 2:
Escribir una función en Python que reciba 2 palabras de igual longitud y retorne verdadero o falso según sean falsos palíndromos o no (un falso palindromo es una palabra que puede leerse de izquierda a derecha y de derecha a izquierda pero tiene significados diferentes. Ejemplo: amor y roma; zorra y arroz).
'''

def obtener_palindromo(palabra1,palabra2):
    bandera = True
    for letra in range(len(palabra1)):
        almacen1 = palabra1[letra]
        almacen2 = palabra2[len(palabra2) - 1 -letra]
        if almacen1 != almacen2:
            bandera = False

    return bandera




def main():
    palabra1 = 'Arroz'
    palabra2 = 'zorrA'
    print(f'{palabra1} y {palabra2} son palindromos? Es {obtener_palindromo(palabra1, palabra2)}')


main()