'''
Ahora quiero que devuelvas la posición del mayor.

Ejemplo:

lista = [8,2,15,6,11]

Debe devolver:

2

Restricciones
❌ No usar index().
❌ No usar max().
❌ No usar sort().
'''

def posicionmayor(lista):
    pos_mayor = 0
    num_mayor = lista[0]
    for i in range(len(lista)):
        if lista[i] > num_mayor:
            num_mayor = lista[i]
            pos_mayor = i
    return pos_mayor





def main():
    lista = [8,2,15,6,11]
    print(posicionmayor(lista))
main()