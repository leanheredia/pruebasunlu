'''
Ejercicio: El Analizador de Divisores Estricto
Descripción:
Deberás desarrollar un programa que solicite al usuario ingresar números enteros para analizarlos. El sistema debe funcionar de manera continua y detenerse de forma automática únicamente cuando el usuario ingrese el número 0 o cualquier valor negativo.
Por cada número positivo ingresado, el programa debe encontrar, contar y clasificar todos sus divisores exactos.
Reglas y Restricciones:
Ejecución continua: El programa debe mantenerse pidiendo y analizando números uno tras otro hasta que se detecte el valor de corte (<= 0).
Búsqueda exhaustiva: Para cada número válido, el programa debe iterar matemáticamente todos los enteros desde el 1 hasta el propio número ingresado para comprobar cuáles lo dividen de forma exacta (es decir, que el resto de la división sea cero).
Clasificación interna: Inmediatamente después de confirmar que un número es divisor, el programa debe realizar una segunda evaluación dependiente de la primera para clasificar si ese divisor en particular es par o impar.
Procesamiento 100% manual: Está estrictamente prohibido utilizar funciones analíticas nativas de colección o conteo (como sum(), count(), len(), max(), min()) o guardar información en listas o arreglos. Todos los cálculos deben realizarse utilizando variables numéricas gestionadas paso a paso por el programador.
Reporte de resultados: Antes de solicitar el siguiente dato, el programa debe mostrar en pantalla el reporte del número analizado indicando: la cantidad total de divisores encontrados, cuántos de esos divisores resultaron pares y cuántos impares.
'''

#ingresar numeros enteros
#validar numero <= 0
#por cada numero, contar y clasificar los divisores (resto de la division == 0)
#ver si ese divisor es par o impar

numero = input('Ingresa un numero entero: ')
divisores = 0

while not (numero.isdigit()) or int(numero) <= 0:
    if not (numero.isdigit()):
        print('Error. Solo se permiten numeros enteros: ')
    else:
        print('Error. Solo se permiten numeros > 0.')
    numero = input('Ingresa un numero entero: ')
numero = int(numero)
for i in range(1,numero):
   