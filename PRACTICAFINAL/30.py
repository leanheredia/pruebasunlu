'''
Una empresa de videojuegos registra las partidas de sus jugadores mediante dos listas paralelas:

lista_jugador
lista_mapa

Cada posición representa una partida realizada.

Ejemplo:

lista_jugador = ["ANA","LUIS","ANA","PEDRO","LUIS","ANA","PEDRO"]

lista_mapa = ["BOSQUE","CIUDAD","DESIERTO","BOSQUE","CIUDAD","CIUDAD","DESIERTO"]

Se pide realizar las siguientes funciones:

A)

Implementar una función:

mas_mapas(lista_jugador, lista_mapa)

que retorne el nombre del jugador que jugó en la mayor cantidad de mapas distintos.

En el ejemplo:

ANA → BOSQUE, DESIERTO, CIUDAD → 3 mapas
LUIS → CIUDAD → 1 mapa
PEDRO → BOSQUE, DESIERTO → 2 mapas

Debe retornar:

"ANA"
'''



def mas_mapas(lista_jugador, lista_mapas):
    for jugador in lista_jugador:

        for i in range(len(lista_mapas)):
            if jugador == lista_jugador[i]:
                for mapa in lista_mapas:
                    if 







def main():
    lista_jugador = ['ANA', 'LUIS', 'ANA', 'PEDRO', 'LUIS', 'ANA', 'PEDRO']
    lista_mapas = ['BOSQUE', 'CIUDAD', 'DESIERTO', 'BOSQUE', 'CIUDAD', 'CIUDAD', 'DESIERTO']
    print(mas_mapas(lista_jugador, lista_mapas))