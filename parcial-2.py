'''Se desea registrar y analizar el desempeño del equipo de Handball de la UNLu en el Campeonato 2026. Para ello, se solicita escribir, en Python, las funciones necesarias con sus correspondientes parámetros por valor o referencia -según corresponda-, para realizar las siguientes tareas:
a)    Definir y cargar en la estructura de datos adecuada el resultado de los 20 partidos del torneo de la siguiente manera: ‘T’ triunfo, ‘D’ derrota, ‘E’ empate y ‘N’ no jugado. Se debe validar que el carácter ingresado sea válido.
b)    Desarrollar una función que retorne un booleano al programa principal indicando true en caso de que el equipo haya jugado todos los partidos del campeonato y false en caso contrario.
c)    Escribir una función que calcule y retorne la cantidad de puntos obtenidos durante el campeonato teniendo en cuenta que por cada victoria se obtienen 3 puntos y por cada empate 1 punto.
d)    Escribir una función que informe el porcentaje de partidos ganados, perdidos, empatados y no jugados durante el campeonato.
'''
partidos = []
resultado_partidos = ['T', 'E', 'D', 'N']

for i in range(20):
    anotar = input(f'Ingrese el resultado del partido {i+1}: ')
    while (anotar != 't' and anotar != 'e' and anotar != 'd' and anotar != 'n'):
        print('Invalido.')
        anotar = input(f'Ingrese el resultado del partido {i+1}: ')
    if 