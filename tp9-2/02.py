'''
Una empresa de ventas de Alemania paga a sus empleados un salario fijo de 5000 euros, más una comisión de 200 euros por cada venta realizada, más el 8 % del valor de esas ventas. Diseña una función que calcule y devuelva el sueldo correspondiente en un mes determinado, recibiendo la cantidad de ventas realizadas por un empleado y el valor total de las mismas.

'''
from mis_funciones import sueldo
def main():
    ventas = int(input('Ingresa la cantidad de ventas: '))
    valor_venta = int(input('Ingresa el total vendido: '))
    calculo = sueldo(ventas, valor_venta)
    print(f'El sueldo total es de {calculo}')

main()