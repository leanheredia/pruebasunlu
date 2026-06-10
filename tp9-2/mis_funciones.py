'''
1. Diseña una función que calcule y retorne la suma de las cifras de un número entero positivo de 4 cifras. 

'''








'''
Una empresa de ventas de Alemania paga a sus empleados un salario fijo de 5000 euros, más una comisión de 200 euros por cada venta realizada, más el 8 % del valor de esas ventas. Diseña una función que calcule y devuelva el sueldo correspondiente en un mes determinado, recibiendo la cantidad de ventas realizadas por un empleado y el valor total de las mismas.

'''

def sueldo(ventas, valor_venta):
    salario = 5000
    if ventas > 0:
        salario += 200 * ventas
        porcentaje_venta = valor_venta * 0.08
        salario += porcentaje_venta
    return salario

'''

3.Un millonario excéntrico tenía tres hijos: Carlos, José y Marta. Al morir dejó el siguiente legado: A José le dejó 4/3 de lo que le dejó a Carlos. A Carlos le dejó 1/3 de su fortuna. A Marta le dejó la mitad de lo que le dejó a José. Diseña una función que calcule y devuelva la suma a repartir y la herencia que recibió cada hijo.

'''
















def precio_final(costo):
    print(costo*0.08)
    resultado = costo+(costo*0.08)